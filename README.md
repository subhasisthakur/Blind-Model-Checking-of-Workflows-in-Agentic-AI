An AI agent’s workflow in response to a task given by the end user in natural language may lead to
undesirable outcomes due to probabilistic error from its large language model. Hence, it is necesary
to ensure the workflow to be executed by an agent is safe. In many cases, the end user may not
have access to the internal model of the agent and hence its intended workflow. In such cases, it
is necessary to perform verification of the safety of an agent’s workflow without the knowledge
of the workflow. In this paper, we address this problem using a zero-knowledge proof for model
checking the agent’s workflow where the verifer(the end user) does not have access to the workflow.
We have developed such verification protocols to check whether the workflow leads to undesirable
states or cycles. We prove that these verificaiton protocols are correct and sound. 
