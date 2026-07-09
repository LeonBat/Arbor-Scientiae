############
# This script ingests the mock run data into the database for testing purposes.
############


############
# This script ingests the mock run data into the database for testing purposes.
############


import json
from pathlib import Path

# defining paths
tests_dir = Path(__file__).resolve().parents[1]
source_path = tests_dir / "mock_papers.json"
output_path = tests_dir / "test_data.json"

#reading json file
with source_path.open("r", encoding="utf-8") as source_file:
	papers = json.load(source_file)

#writing jsonfile content to test_data.json
with output_path.open("w", encoding="utf-8") as output_file:
	json.dump(papers, output_file, indent=2, ensure_ascii=False)

#load content of test_data.json
with output_path.open("r", encoding="utf-8") as written_file:
	written_papers = json.load(written_file)



#Checking for correctness

#Is papers a list?
assert isinstance(papers, list), "Expected a list of papers"
# Does the list contain 5 papers
assert len(papers) == 5, f"Expected 5 papers, got {len(papers)}"

# Checks the first paper with all fields
first_paper = papers[0]
assert first_paper["paperId"] == "paper_001"
assert first_paper["title"] == "Attention Is All You Need"
assert len(first_paper["citations"]) == 2
assert len(first_paper["references"]) == 3
assert len(first_paper["authors"]) == 8


# Compares the read papers with the written papers
assert written_papers == papers, "Roundtrip write/read mismatch"

#Final statement for giving overview
print(f"Loaded {len(papers)} papers from {source_path.name} and wrote {output_path.name}.")
print(f"First paper title: {first_paper['title']}, with {len(first_paper['citations'])} citations and {len(first_paper['references'])} references.")
print(f"First paper authors: {[author['name'] for author in first_paper['authors']]}")

