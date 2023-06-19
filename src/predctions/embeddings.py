from sentence_transformers import SentenceTransformer

def gen_embeddings(data: str)->list:
    #Define the model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    #Start the multi-process pool on all available CUDA devices
    pool = model.start_multi_process_pool(['cpu', 'cpu', 'cpu'])

    #Compute the embeddings using the multi-process pool
    final_emb = model.encode_multi_process(data, pool)
    print("Embeddings computed. Shape:", final_emb.shape)

    #Optional: Stop the proccesses in the pool
    model.stop_multi_process_pool(pool)

    return final_emb