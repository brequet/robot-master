package pkg

import (
	"bytes"
	_ "embed"
	"encoding/json"
	"fmt"
	"os/exec"
)

//go:embed python/get-robot-data.py
var getDataScript string

type Test struct {
	Name string `json:"name"`
}

type Suite struct {
	Name  string `json:"name"`
	Tests []Test `json:"tests"`
}

func ExecuteGetDataScript() ([]Suite, error) {
	var buf bytes.Buffer
	buf.WriteString(getDataScript)

	cmd := exec.Command("python")
	cmd.Stdin = &buf

	var stdout, stderr bytes.Buffer
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr

	err := cmd.Run()
	if err != nil {
		fmt.Printf("Execution failed with error: %v\n", err)
		fmt.Printf("Stdout output:\n%s", stdout.String())
		fmt.Printf("Stderr output:\n%s", stderr.String())
		return nil, err
	}

	var suites []Suite
	if err := json.Unmarshal(stdout.Bytes(), &suites); err != nil {
		fmt.Printf("Failed to decode JSON: %v\n", err)
		return nil, err
	}

	return suites, nil
}
