package pkg

import (
	"encoding/json"
	"os"
	"path/filepath"
	"reflect"
	"testing"
)

func TestExecuteGetDataScript(t *testing.T) {
	// Read the expected JSON from the file
	expectedFilePath := filepath.Join(".", "test-data", "robot-structure-example.json")
	expectedContent, err := os.ReadFile(expectedFilePath)
	if err != nil {
		t.Fatalf("Failed to read expected JSON file: %v", err)
	}

	// Execute the script and get the result
	result, err := ExecuteGetDataScript() // This now returns a slice of Category
	if err != nil {
		t.Fatalf("Failed to execute script: %v", err)
	}

	// Unmarshal the expected JSON into a slice of Category
	var expectedCategories []Suite
	if err := json.Unmarshal(expectedContent, &expectedCategories); err != nil {
		t.Fatalf("Failed to unmarshal expected JSON: %v", err)
	}

	// Compare the slices of Category
	if !reflect.DeepEqual(expectedCategories, result) {
		t.Errorf("Expected categories do not match result.")
	}
}
