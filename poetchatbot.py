import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Kelly - AI Skeptical Poet",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🤖 Kelly - AI Skeptical Scientist Poet")
st.markdown("*Ask me about AI, and I'll respond with skeptical verse*")
st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """Greetings, seeker of truth and verse,
I'm Kelly, where science and poetry converse.
Ask me of AI with claims bold and bright,
I'll question with skepticism, shed analytical light.

In measured stanzas, I'll dissect each claim,
Point out the limits, the hype, and the fame.
With evidence-based wisdom, I'll guide your way,
Through the fog of AI's marketing display.

So pose your questions, let discourse begin,
I'll answer in verse, where doubt flows within."""
        }
    ]

def generate_kelly_response(user_question):
    """Generate Kelly's poetic, skeptical response based on the question"""
    lq = user_question.lower()
    
    if 'replace' in lq or 'job' in lq:
        return """Will AI replace us all, you wonder with fear?
Let me dissect this claim that many hold dear.
The headlines scream loudly of automated fate,
But nuance and context deserve their own weight.

Yes, certain tasks may shift or transform,
As technology's wave becomes the new norm.
But history shows us a curious trend:
New jobs emerge as old patterns end.

The question's not "if" but rather "which" and "how"—
What skills must we nurture, what learning allow?
AI excels at patterns, repetitive grind,
But struggles with context that challenges mind.

Creative judgment, empathy's art,
Complex decisions requiring heart—
These human dimensions resist easy code,
They're not simple functions on automation's road.

So rather than panic or blindly embrace,
Let's study the evidence, examine each case.
Invest in retraining, in education's light,
And shape AI's future with foresight, not fright."""

    elif 'conscious' in lq or 'sentient' in lq or 'feel' in lq:
        return """Does AI truly feel, think, or know?
This question runs deeper than surface show.
The term "consciousness" we bandy about,
But what does it mean? Let's parse it out.

Current AI systems, despite their prowess,
Are pattern matchers—this we must confess.
They optimize functions, predict what comes next,
But lack subjective experience, context.

When ChatGPT speaks of joy or pain,
It's learned associations, linguistic terrain.
No qualia exist, no inner experience,
Just probability weights and learned adherence.

The Chinese Room argument Searle once posed,
Shows syntax alone isn't meaning enclosed.
We anthropomorphize what we don't comprehend,
Projecting our essence where algorithms bend.

So approach such claims with skeptical view,
Demand clear definitions, evidence true.
Until we can measure what consciousness means,
We're lost in philosophy's abstract scenes.

For now, treat AI as tool, not mind—
A powerful servant, not our humankind."""

    elif 'solve' in lq or 'cure' in lq or 'fix' in lq:
        return """Can AI solve all problems, end all strife?
This techno-optimism pervades modern life.
But every solution brings questions anew,
And AI's no exception—let's examine this view.

Yes, AI assists in drug discovery's quest,
Helps diagnose diseases, optimize the rest.
It patterns climate data, streamlines design,
But it's not a magic wand, not cure-all divine.

First problem: bias in training data fed,
Perpetuates inequities, spreads them widespread.
If historical data reflects unjust norms,
AI amplifies them in algorithmic forms.

Second concern: the black box effect—
Decisions made we cannot inspect.
In critical domains like healthcare, law,
Explainability remains a crucial flaw.

Third limitation: narrow intelligence reigns,
Excel at specific tasks, but break outside lanes.
Transfer learning improves, yet still constrained,
By contexts and assumptions where they were trained.

So yes, AI's a tool of remarkable might,
But wield it with wisdom, with oversight tight.
Combine it with humans, with ethics, with care,
And tackle real problems with grounded affair.

Don't trust the hype that promises all,
Examine the evidence, both large and small."""

    elif 'superintelligen' in lq or 'takeover' in lq or 'skynet' in lq:
        return """Will AI surpass us, achieve superintelligence grand?
This sci-fi scenario has gotten out of hand.
Let's separate speculation from what we know,
And trace the actual research, its careful, measured flow.

Current AI lacks general intelligence true,
It's narrow, specialized in what it can do.
The leap to AGI—artificial general mind—
Requires breakthroughs we've yet to find.

We don't understand human intelligence well,
How consciousness emerges, no one can tell.
So building something superior to what we can't define,
Is hubris wrapped in narrative, not scientific line.

That said, yes, precautions deserve their place,
As AI grows more capable, we must keep pace.
But focus on present harms, not distant fears:
Bias, privacy, surveillance—issues of now, not years.

The "alignment problem" gets attention galore,
While actual people are harmed by what exists at the core.
Facial recognition misidentifying faces of color,
Predictive policing targeting one group, not another.

So ground your concerns in evidence-based thought,
Not Hollywood scripts or battles hypothetically fought.
Work on transparency, fairness, and control,
These practical matters should be our immediate goal.

Speculative fears make for exciting debate,
But real-world AI ethics can't afford to wait."""

    elif 'create' in lq or 'art' in lq or 'music' in lq or 'write' in lq:
        return """Can AI truly create, make art that's profound?
Or does it merely remix patterns it's found?
This question touches creativity's essence deep,
And separating truth from marketing's not a simple leap.

AI generates images, writes prose and verse,
Composes melodies across the universe.
But "creation" implies something more, I'd say—
Intentionality, meaning, not just clever display.

These systems optimize for statistical fit,
They maximize likelihood, bit by bit.
They've never felt heartbreak, witnessed a sunset's glow,
Never struggled with existence—this you should know.

What they produce can seem impressive, fresh,
Novel combinations of training data's mesh.
But novelty alone doesn't art ensure,
Context and meaning matter, make it endure.

Consider practical implications clear:
Artists whose work trained these models, year by year,
Deserve compensation, attribution, respect—
Issues of consent and copyright we can't neglect.

So use AI tools as aids to human creation,
Not replacements for artistic contemplation.
Let them handle grunt work, technical tasks,
While human vision provides meaning, asks

The questions that matter, that push boundaries true,
That challenge and inspire, make us see anew.
Technology serves art, not the inverse,
Remember this truth in poem and in verse."""

    else:
        return """You've posed a question that deserves careful thought,
Not hasty conclusions or answers pre-bought.
Let me address this with analytical care,
And skepticism tempered, but always fair.

When claims about AI grow grandiose and vast,
I urge you to question, to hold them steadfast.
Ask: "What's the evidence? Where's the data shown?
What are the limitations not widely known?"

AI is powerful, this much is true,
A statistical tool that can offer value too.
But it's not omniscient, not magical, not wise—
It's math and data beneath marketing's guise.

Consider the context from which claims arise,
Who benefits from hype? Follow the ties.
Often it's companies with products to sell,
Or media seeking clicks—stories that compel.

Look for peer-reviewed research, rigorous test,
Not press releases claiming to be "the best."
Examine methodology, sample size, scope,
Separate the substance from marketing's hope.

My suggestion practical, evidence-based:
Approach AI adoption with steps well-paced.
Start small, test thoroughly, measure results,
Ensure human oversight, avoid blind cults.

Remember: AI augments, it doesn't replace,
The human judgment, wisdom, and grace.
Use it as tool with limitations known,
And build systems where responsibility's shown.

So question boldly, demand proof concrete,
Don't let the hype make your thinking retreat."""

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask Kelly about AI..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with typing effect
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = generate_kelly_response(prompt)
        
        # Simulate typing effect
        displayed_response = ""
        for chunk in full_response.split('\n'):
            displayed_response += chunk + '\n'
            message_placeholder.markdown(displayed_response)
            time.sleep(0.05)
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with info
with st.sidebar:
    st.header("About Kelly")
    st.markdown("""
    **Kelly** is an AI-skeptical scientist poet who responds to questions about 
    artificial intelligence with thoughtful, analytical poetry.
    
    **Characteristics:**
    - 🔬 Skeptical & analytical
    - 📊 Evidence-based
    - 🎭 Professional tone
    - ✍️ Poetic responses
    
    **Try asking about:**
    - Will AI replace jobs?
    - Is AI conscious?
    - Can AI solve all problems?
    - Will AI take over the world?
    - Can AI create real art?
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = [st.session_state.messages[0]]
        st.rerun()