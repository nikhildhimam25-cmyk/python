# import os
# import streamlit as st
# from dotenv import load_dotenv
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain_community.vectorstores import FAISS
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()

# # --- Sidebar for PDF upload ---
# st.sidebar.title("Upload Your Knowledge Base")
# uploaded_files = st.sidebar.file_uploader("Upload PDF(s)", type=["pdf"], accept_multiple_files=True)

# # Initialize session state for vector store
# if "vectorstore" not in st.session_state:
#     st.session_state.vectorstore = None

# # Process uploaded PDFs
# if uploaded_files:
#     documents = []
#     for file in uploaded_files:
#         # Save uploaded file temporarily
#         with open(file.name, "wb") as f:
#             f.write(file.getbuffer())
#         loader = PyPDFLoader(file.name)
#         documents.extend(loader.load())
    
#     # Split documents into chunks
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     splits = text_splitter.split_documents(documents)
    
#     # Create embeddings and vector store
#     embeddings = OpenAIEmbeddings()
#     vectorstore = FAISS.from_documents(splits, embeddings)
#     st.session_state.vectorstore = vectorstore
    
#     st.sidebar.success(f"Processed {len(documents)} pages! Ready to chat.")
#     # Clean up temp files
#     for file in uploaded_files:
#         os.remove(file.name)

# # --- Main Chat Interface ---
# st.title("📄 RAG Chatbot - Ask Questions About Your Documents")

# if st.session_state.vectorstore is None:
#     st.info("Upload PDFs in the sidebar to start.")
# else:
#     # LLM setup
#     llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
#     # Prompt template
#     system_prompt = (
#         "You are an assistant for question-answering tasks. "
#         "Use the following pieces of retrieved context to answer "
#         "the question. If you don't know the answer, say that you "
#         "don't know. Use three sentences maximum and keep the "
#         "answer concise."
#         "\n\n"
#         "{context}"
#     )
#     prompt = ChatPromptTemplate.from_messages(
#         [
#             ("system", system_prompt),
#             ("human", "{input}"),
#         ]
#     )
    
#     # Create RAG chain
#     retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3})
#     question_answer_chain = create_stuff_documents_chain(llm, prompt)
#     rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
#     # Chat history
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
    
#     # Display chat messages
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])
    
#     # User input
#     if prompt_input := st.chat_input("Ask a question about your documents..."):
#         st.session_state.messages.append({"role": "user", "content": prompt_input})
#         with st.chat_message("user"):
#             st.markdown(prompt_input)
        
#         with st.chat_message("assistant"):
#             with st.spinner("Thinking..."):
#                 response = rag_chain.invoke({"input": prompt_input})
#                 answer = response["answer"]
#                 st.markdown(answer)
        
#         st.session_state.messages.append({"role": "assistant", "content": answer})