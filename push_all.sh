#!/bin/bash
# Push All Repositories Helper Script

MSG="${1:-Auto-update}"

echo "=========================================="
echo "🚀 Syncing and Pushing All Repositories..."
echo "=========================================="

# 1. CineSage Repo
if [ -d "CineSage/.git" ]; then
    echo "\n📂 Checking CineSage..."
    cd CineSage
    if [[ -n $(git status --porcelain) ]]; then
        echo "  ➜ Changes found in CineSage. Committing and pushing..."
        git add .
        git commit -m "$MSG"
        git push origin main
    else
        echo "  ✓ CineSage is up to date."
    fi
    cd ..
fi

# 2. CineSage2.0 Repo
if [ -d "CineSage2.0/.git" ]; then
    echo "\n📂 Checking CineSage2.0..."
    cd CineSage2.0
    if [[ -n $(git status --porcelain) ]]; then
        echo "  ➜ Changes found in CineSage2.0. Committing and pushing..."
        git add .
        git commit -m "$MSG"
        git push origin main
    else
        echo "  ✓ CineSage2.0 is up to date."
    fi
    cd ..
fi

# 3. Parent GenerativeAI Repo
echo "\n📂 Checking Parent Repo (GenerativeAI)..."
if [[ -n $(git status --porcelain) ]]; then
    echo "  ➜ Changes found in Parent Repo. Committing and pushing..."
    git add .
    git commit -m "$MSG"
    git push origin main
else
    echo "  ✓ Parent Repo is up to date."
fi

echo "\n=========================================="
echo "✨ All repositories synced & pushed successfully!"
echo "=========================================="
