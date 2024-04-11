# Intelligent Sensing Lab Website

## Develop

```sh
bundle exec jekyll serve
```

### Add Publications

Create a new markdown document in `_papers`. You can technically name it anything, but it is best to either use your full paper title, or the acronym/"key" before the colon in your paper. The first word will be used in the generated BibTex entry. The contents should look like:

```md
---
title: full paper title
authors:
    - Author One
    - Author Two
	- ...
links:
    paper: ...
	...
venue: ...
date: publish date (only year is displayed, month/day matter for sorting)
---

Full abstract

Optionally more elements you would like to display on the paper's "read more" page.
```

Optional items:

-   Add a thumbnail/icon image to `assets/images/papers/icons` named the exact same as your markdown file and in `.webp` format. Ideally also crop/resize the image to a square at most 300x300.
-   Add a teaser image to `assets/images/papers/teasers` named the exact same as your markdown file and thumbnail in `.png` format.
-   Add any new collaborator personal websites to `_data/collaborators.yml`.
