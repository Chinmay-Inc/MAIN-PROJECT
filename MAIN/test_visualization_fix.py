"""
Test script to verify the visualization fix
"""
import sys
import traceback

def test_visualization_fix():
    """Test the visualization fix for empty data"""
    try:
        print("Testing visualization fix...")
        
        # Test 1: Import modules
        from visualizations import InvestmentVisualizer
        print("✅ InvestmentVisualizer imported successfully")
        
        # Test 2: Create visualizer instance
        visualizer = InvestmentVisualizer()
        print("✅ InvestmentVisualizer created successfully")
        
        # Test 3: Test with empty data
        fig = visualizer.create_pie_chart({})
        print("✅ Empty pie chart created successfully")
        
        # Test 4: Test with None data
        fig = visualizer.create_pie_chart(None)
        print("✅ None pie chart created successfully")
        
        # Test 5: Test with invalid data structure
        fig = visualizer.create_pie_chart({"invalid": "data"})
        print("✅ Invalid data pie chart created successfully")
        
        # Test 6: Test with valid data structure
        valid_data = {
            "stocks": {"percentage": 40, "amount": 4000, "description": "Individual stocks"},
            "bonds": {"percentage": 30, "amount": 3000, "description": "Government bonds"},
            "cash": {"percentage": 30, "amount": 3000, "description": "Cash and equivalents"}
        }
        fig = visualizer.create_pie_chart(valid_data)
        print("✅ Valid data pie chart created successfully")
        
        print("\n🎉 All visualization tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_visualization_fix()
    sys.exit(0 if success else 1)
