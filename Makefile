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

# upload-research-papers: 
upload-research-papers:
	@python fetchXML.py

# download-form-data
download-sheets-data:
	@python accessGoogleSheets.py

# Display help information
help:
	@echo "Available commands:"
	@echo "  build     				: Build the Jekyll site"
	@echo "  serve				: Serve the Jekyll site locally"
	@echo "  clean     				: Remove the generated files"
	@echo "  install   				: Install project dependencies"
	@echo "  update    				: Update project dependencies"
	@echo "  help      				: Display this help message"
	@echo "  upload-research-papers 		: Upload research papers"
	@echo "  download-sheets-data 		: Download form sheets data"

.PHONY: build serve clean install update upload-research-papers download-sheets-data help
