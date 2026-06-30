# tests/test_agent.py
# VibeShield — Agent tests (placeholder)
"""
Module: test_agent.py
Description: QA Unit Testing Suite for verifying the State Graph Finite State Machine 
             (FSM) boundaries, compliance routing, and error recovery channels.
"""

import sys
import os
import unittest

# Ensure the app directory is accessible to the testing execution path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.agent import AgentState, start_node, audit_node, router_conditional_edge, repair_node, end_node

class TestVibeShieldGraphPipeline(unittest.TestCase):
    """Encapsulates execution validation cases for the core routing graph."""

    def test_pipeline_compliant_flow(self):
        """
        Asserts that a standard, fully compliant workspace state bypasses 
        the recovery node and routes directly to completion.
        """
        state = AgentState()
        
        # Force a baseline compliant simulation state
        state = start_node(state)
        state["validation_status"] = "COMPLIANT"
        
        # Evaluate the router decision vector
        routing_vector = router_conditional_edge(state)
        self.assertEqual(routing_vector, "end", "Failed: Compliant state should route directly to 'end'.")
        
        state = end_node(state)
        self.assertEqual(state["current_step"], "EXECUTION_COMPLETE")

    def test_pipeline_recovery_loop_flow(self):
        """
        Asserts that a non-compliant layout state correctly trips the conditional 
        routing edge, routes to repair_node for correction, and completes safely.
        """
        state = AgentState()
        state = start_node(state)
        
        # Simulate a strict compliance failure discovered during audit
        state["validation_status"] = "NON_COMPLIANT"
        
        # The router must detect this and enforce the repair branch
        routing_vector = router_conditional_edge(state)
        self.assertEqual(routing_vector, "repair", "Failed: Non-compliant state must route to 'repair'.")
        
        # Trigger the repair node recovery routine
        if routing_vector == "repair":
            state = repair_node(state)
            self.assertEqual(state["validation_status"], "COMPLIANT", "Failed: Repair node did not correct status.")
            
            # Re-evaluate routing after structural correction
            routing_vector = router_conditional_edge(state)
            self.assertEqual(routing_vector, "end", "Failed: Post-repair state should route to 'end'.")
            
        state = end_node(state)
        self.assertEqual(state["current_step"], "EXECUTION_COMPLETE")

if __name__ == "__main__":
    unittest.main()