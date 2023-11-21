

def read_item_block(block_id: int, query_param_lol: str = None):
    print(f"log : {block_id} , {query_param_lol}")
    return {"block_id": block_id, "query_param": query_param_lol}