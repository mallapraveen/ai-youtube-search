import faiss

class faiss_db:
    def __init__(self,d) -> None:
        #Initializing the index
        self.index=faiss.IndexFlatL2(d)

        #checking whether the index is trained
        print(self.index.is_trained)

    def storing_vectors(self,final_emb: list)->None:

        #Adding the embeddings in the index
        self.index.add(final_emb)

        #Total number of embeddings added
        print(self.index.ntotal)
