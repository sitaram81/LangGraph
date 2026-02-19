Definition of Agentic AI
Agentic AI refers to artificial intelligence systems that exhibit agency—the capacity to act independently, set goals, and execute tasks with minimal human intervention. Unlike traditional AI, which mainly analyzes data or responds to commands, agentic AI is designed to plan, adapt, and take purposeful actions toward achieving objectives.

Key Characteristics:

    • Autonomous
    • Goal Oriented
    • Planning
    • Reasining
    • Adaptability
      Context Awarness
Autonomy:

Autonomy refers to the AI system's ability to make decision and take actions on its own to achieve a given goal, without needing step-by-step human instructions.

    1. our AI recruiter is autonomous
    2. It's proactive
    3. Autonomy in multiple facets
        a. Execution
        b. decision making
        c. Tool usages
    4. Autonomy can be controlled
        a. Permission scope: Limit what tools or actions the agent can perform independently. (Can screen candidates, but needs approval before rejecting anyone)
        Human-in-the-loop (HITL) 	Insert checkpoint where human approval is required before continuing.(Can I post this JD)
        Override controls	Allow users to stop, pause or change the agents's behaviour at any time. (Pause screening command to halt resume processing.)
        Guardrails / Policies 	Define hard rules or ethical boundaries the agent must follow (Nevelr schedule interviews on weekends.)
    
    5. Autonomy can be dangerous:
        a. The application autonomously sends out job offer with incorrect salaries or terms.
        b. The application shortlist candidates by age or nationality, violating anti-discrimination laws.
        c. the application spending extra on linkdin ads.

Goal Oriented:

Being goal-oriented means that the AI system operates with a persistent objective in mind and continuously directs its action to achieve that obective, rather than just responding to isolated prompts.

    1. Goals acts as a compass for Autonomy
    2. Goals can come with constraints
    3. Goals are stored in core memory
    4. Goals can be altered

Planning:

Planning is the agent's ability to break down a high-level goal into a structured sequence of actions or subgoals and decide the best path to achieve the desired outcomes.

Step 1: Generating multiple candidate plans
    ▪ Plan A : Post ID on Linkedin, GitHub Jobs, AngelList
    ▪ Plan B: Use Internal referals and hiring agencies
Step 2: Evaluate each plan:
    ▪ Efficiency (which is faster?)
    ▪ Tools Availability (Which tool are available)
    ▪ Cost (Does it require premium tools?)
    ▪ Risk (Will it fall if we get no applicants?)
    ▪ Alignment with constraints (Remote-only?Budgets?)
Step 3: Select the best plan with the help of:
    ▪ Human-in-the-loop input (eg. "Which of these options do you prefer?")
    ▪ A pre programmed policy (eg. "Favor low-cost channels first")
    
Reasoning:

Reasoning is the cognitive process through which an agentic AI system interprets information, draws conclusion, and makes decision - both while planning ahead and while executing  actions in real time.

Reasoning During Planning:

    Goal Decomposition 	Break down abstract goals into concreted steps
    Tool selection 	Decide which tools will be needed for which steps
    Resource estimation  	Estimate time, dependencies, risks

Reasoning During Execution:

    Decision Making 	 Choosing between options (Candidate metrics ð schedule best, reject
    HITL handling 	 Knowing when to pause and ask for help (unsure about salary range)
    Error handling 	 Interpreting tools/API failures and recovering

Adaptability:

Adaptability  is the agent's ability to modify its plans, stratergies, or actions in response to unexpected conditions- all while staying aligned with the goal.
    1. Failures (Calendar API)
    2. External Feedback (Less no or applications)
    3. Changing goals (Hiring a freelancer)

Context Awareness:

Contect awareness is the agent's ability to understand, retain, and utilize relevant information from the ongoing task, past interaction, user preferences, and enviornmental cues to make better decisions throughout a multiple-step process.

    1. Types of context
        a. The original goal
        b. Progress till now + interaction history  ( job description was finalized and posted to linkedin & Github jobs)
        c. Enviornment state (Number of applicants so far - 8 or linkedin promotion ends in 7 days)
        d. Tool responses (Resume parser -> Candiate has 3 years of experience in Djano - AWS programming or canlendar API - Candidate available for interview on wedensday 2pm)
        e. User Specific perference: Perference remote first candidate or likes receiving interview questions in a google docs)
        f. Policy or Gardrals  ( do not send offer without explicit  user approval or Never use platforms that requires paid ads unless approved)
    2. Context awareness is implented through memory
    3. Short term memory - (curren session related)
    4. Long term memory - 
    
Agnetic highlevel Components: 

    1. Brain 
    2. Orchestrator
    3. Tools
    4. Memory
    5. Supervisor

Brain (LLM):

Goal Interpretations  	Understands user instructions and translates them into objectives.
Planning  	Break down high level goals into subgoals and ordered steps.
Reasoning 	Make decisions, resolve ambiguity and evaluates trade-offs.
Tool Selection 	Choose which tool(s) to use at a given step.
Communication 	Generate natural language outputs for human or other agents.

Orchestrator (LangGraph):

Task Sequencing	Determine the order of actions (Step 1, Step 2 .....)
Conditional Routing 	Directs flow based on context (eg. if failure, retry or escalate)
Retry Logic	Handles failed tool calls or reasonings attempts with backoff
Looping & Iterations 	Repeats steps (eg. keep checking job apps until 10 are received)
Delegation	Decide whether to hand off works to tools, LLM or human

Tools:

External Action	Perform API Calls (eg. post a job, send an email, trigger onboarding)
Knowledge Base Access	Retrieve factual or domain-specific information using RAG or search tools to ground responses.

Memory: 

Short-Term memory 	Maintains the active session contexts - Recent user messages, tool calls and immediate decisions.
Long-Term Memory 	Persists high level goals, past interactions, user perferences and decision across sessions.
State Tracking 	Monitors progress what's completed, what's pending (eg. JD posted, offer sent)

Superviosr:

Approval Requests (HITL):Agent checks with human before high-risk actions (eg. sending offers)
Guardrails Enforcement:Blocks unsafe or non-compliant behavior
Edge Case Escalation:Alterts human when uncertainly or conflicts aries.

