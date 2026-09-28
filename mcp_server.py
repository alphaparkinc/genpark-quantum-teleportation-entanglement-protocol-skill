import sys
import json
from client import QuantumTeleportation

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "simulate_quantum_teleportation",
                        "description": "Simulate quantum teleportation of qubit state alpha|0> + beta|1>",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "alpha": {"type": "number"},
                                "beta": {"type": "number"}
                            },
                            "required": ["alpha", "beta"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "simulate_quantum_teleportation":
            tp = QuantumTeleportation(args["alpha"], args["beta"])
            fid = tp.run_protocol()
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"fidelity": fid, "teleported_state": {"alpha": tp.alpha, "beta": tp.beta}})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
