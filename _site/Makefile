# Build the Jekyll site
build:
	@bundle exec jekyll build

# Serve the Jekyll site locally
serve:
	@bundle exec jekyll serve

# Clean the generated files
clean:
	@bundle exec jekyll clean

# Install project dependencies
install:
	@bundle install

# Update project dependencies
update:
	@bundle update

# Update Research Papers
update-papers:
	@python fetchXML.py

# Display help information
help:
	@echo "Available commands:"
	@echo "  build     		: Build the Jekyll site"
	@echo "  serve		: Serve the Jekyll site locally"
	@echo "  clean     		: Remove the generated files"
	@echo "  install   		: Install project dependencies"
	@echo "  update    		: Update project dependencies"
	@echo "  update-papers	: Update the research papers"
	@echo "  help      		: Display this help message"

.PHONY: build serve clean install update update-papers help
