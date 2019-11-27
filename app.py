from flask import Flask, request, render_template
import json
import re

class DocInitialize:
   
    def __init__(self, docId, occurs):
        self.docId = docId
        self.occurs = occurs        

class DocStore:

    def __init__(self):
        self.ds = dict()
  
    def get(self, id):
        return self.ds.get(id, None) 

    def add(self, document):
         return self.ds.update({document['id']: document})

    def remove(self, document):
        return self.ds.pop(document['id'], None)

class InvertedIndex:

    def __init__(self, ds):
        self.index = dict()
        self.ds = ds

    def index_document(self, document):
 
        clean_text = re.sub('[A-Z]+', lambda m: m.group(0).lower(),document['text'])
        terms = clean_text.split(' ')
        occurrence_dict = dict()
        for term in terms:
            term_occurs = occurrence_dict[term].occurs if term in occurrence_dict else 0
            occurrence_dict[term] = DocInitialize(document['id'], term_occurs + 1)
            
        update_dict = { key: [occurrence]
                       if key not in self.index
                       else self.index[key] + [occurrence]
                       for (key, occurrence) in occurrence_dict.items() }
        self.index.update(update_dict)
        self.ds.add(document)

        return document
    
    def search_query(self, query):
        return { term: self.index[term] for term in query.split(' ') if term in self.index }

ds = DocStore()
index = InvertedIndex(ds)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clear',methods=['GET','POST'])
def clear():
    InvertedIndex.index = dict()
    InvertedIndex.ds = ds 
    return render_template('index.html',message="Indexes Cleared")


@app.route('/search', methods=['POST'])
def search():
    ds = DocStore()
    index = InvertedIndex(ds)
    if request.method == 'POST':
        para = request.form['text']
        search_term = request.form['search_text']
         
      
        fw = open('tempStore.txt','w+')
        fw.write(para)
        fw.close()

        fr = open('tempStore.txt','r')
        docs = fr.readlines()
        fr.close()
        docs.append('\n')
        docs.append('\n')

        paragraph = []


        n_count = 0
        val = ""

        for i in docs:

            if (i.count('\n')==1 and len(i)==1):
                n_count+=1

            if n_count==2:
                replaced_val = val.replace('\n',' ')

                paragraph.append(replaced_val)
                val=""
                n_count=0
                continue
            val += i

        count = 0   
        file = []
        for i in paragraph:
            paragraph_dict = {}
            paragraph_dict['id'] = count
            paragraph_dict['text'] = i[:-1]
            data_dict = paragraph_dict
            file.append(data_dict)
            count+=1
      
        for i in range(len(file)):
            index.index_document(file[i])
        
        doc_list = []
        result = index.search_query(search_term)    
        for term in result.keys():
            for occurrence in result[term]:
                
                document = ds.get(occurrence.docId)
                doc_dict = json.dumps(document['text'])
                doc_list.append(doc_dict)
            
        if len(doc_list) == 0:
            return render_template('index.html', message="Search Not Available")

        elif len(doc_list) > 10:
            doc_list = doc_list[:10]

        return render_template('index.html',doc_list=doc_list)


if __name__ == '__main__':
    app.run(debug=True)