from dotenv import load_dotenv 
load_dotenv()  

from prompt_experimentation.run_local import LocalFlowExecution

def main():
    data = "email_classification/data/data.jsonl"
    flow = "email_classification/flows/standard"
    eval_flow = "email_classification/flows/evaluation"
    named_entity_flow = LocalFlowExecution(flow, eval_flow, data, {"email": "${data.email}"})
    named_entity_flow.process_local_flow()
    named_entity_flow.create_local_connections()
    run_ids = named_entity_flow.execute_experiment()

    named_entity_flow.execute_evaluation(run_ids,data,{
                "ground_truth": "${data.truth}",
                "entities": "${run.outputs.categories}",
            })

if __name__ == "__main__":
    main()