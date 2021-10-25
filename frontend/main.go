package main

import (
	"embed"
	"net/http"
	"os"
)

//go:embed dist
var staticFS embed.FS

func main() {
	sessionKey := os.Getenv("SESSION_KEY")
	if sessionKey == "" {
		panic("SESSION KEY NOT SET")
	}
	projectID := os.Getenv("PROJECT_ID")
	if projectID == "" {
		panic("NO PROJECT!")
	}

	// Serve static files
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.FS(staticFS))))

	http.ListenAndServe(":8080", nil)
}
