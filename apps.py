import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool,initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(page_title="Text to maths problem solver and search data assistant",page_icon="🔍",layout="wide")
st.title("Text to maths problm solver using Google Gemma 2")

groq_api_key=st.sidebar.text_input("Enter your groq api key",type="password")

if not groq_api_key:
    st.info("please add your groq api key to continue")
    st.stop()

llm=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikepedia",
    func=wikipedia_wrapper.run,
    description="A tool for search various information on internet"

)

## Maths chain
math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answering maths related queries.Only input mathematical expression are needed"

)
prompt="""You are an agent tasked for solving mathematical question.Logically arrive at solution and display it point wise for the question below.
          Question:{question}
          Answer:
          """
prompt_template=PromptTemplate(input_variables=["question"],template=prompt)

chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning question"
)


###combine all tools into chain
chain=LLMChain(llm=llm,prompt=prompt_template)

assistant_agent=initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assisstant",
         "content":"Hi I am a maths chatbot who answered all your maths related questions."}
    ]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

def generate_response(question):
    response=assistant_agent.invoke({"input":question})

question=st.text_area("Enter your question","I have 5 bananas and 7 grapes.I eat 2 bananas and 3 grapes.How many fruits do I have now?")
if st.button("find my answer"):
    if question:
        with st.spinner("Generate response..."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)
            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
            st.session_state.messages.append({"role":"assistant","content":"response"})
            st.write('### resopnse')
            st.success(response)
else:
    st.warning("please enter the question")

