import xml.dom.minidom
import xml.sax
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = 'C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical 14/go_obo.xml'
ONTOLOGIES = ['molecular_function', 'biological_process', 'cellular_component']

def parse_dom(file_name):
    dom_tree = xml.dom.minidom.parse(file_name)
    terms = dom_tree.getElementsByTagName("term")
    counts = {ontology: 0 for ontology in ONTOLOGIES}
    
    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].childNodes[0].data
        if namespace in counts:
            counts[namespace] += 1
    return counts

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.namespace = ""
        self.counts = {ontology: 0 for ontology in ONTOLOGIES}
    
    def startElement(self, tag, attributes):
        self.current_data = tag
    
    def characters(self, content):
        if self.current_data == "namespace":
            self.namespace = content
    
    def endElement(self, tag):
        if tag == "namespace":
            if self.namespace in self.counts:
                self.counts[self.namespace] += 1
        self.current_data = ""

def parse_sax(file_name):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = GOHandler()
    parser.setContentHandler(Handler)
    parser.parse(file_name)
    return Handler.counts

def plot_data(counts, title):
    ontologies = list(counts.keys())
    frequencies = list(counts.values())
    plt.figure(figsize=(10, 5))
    plt.bar(ontologies, frequencies, color='skyblue')
    plt.xlabel('Ontologies')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()

start_time_dom = datetime.now()
dom_counts = parse_dom(FILE_NAME)
time_dom = datetime.now() - start_time_dom

start_time_sax = datetime.now()
sax_counts = parse_sax(FILE_NAME)
time_sax = datetime.now() - start_time_sax

print("DOM Counts:", dom_counts)
print("DOM Time:", time_dom)
print("SAX Counts:", sax_counts)
print("SAX Time:", time_sax)

plot_data(dom_counts, 'DOM Parsing Results')
plot_data(sax_counts, 'SAX Parsing Results')
