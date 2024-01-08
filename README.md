# mkdoc-site

I did this website with `mkdoc` from scratch with the (brilliant) tutorial video at [here](https://www.youtube.com/watch?v=Q-YA_dA8C20).

It requires .
- Create a Github repo and clone it locally
- Create and activate a virtual env and `pip install mkdocs-material`.
- Cd to the clone dir.
- `mkdoc new .` to generate mkdocs.yaml and doc/index.md (the very basic structure of the site)
- Serve the site locally with `mkdoc serve`. The command will provide a http adress to copy in the adress bar of the brwoser.
- Build up the site and check it on the locally served pages.
- Create the github action (i.e. the `.github/workflows/ci.yml`).
- Commit/push to the GH repo.

On the GitHub repo, we need to set that it is Github Pages. `Settings/Pages/`. Deploy from branch and choose the branch `gh-pages` that has just been created by the `ci.yml` file.

The CI then processes the required action and in `Actions/pages build and deployment/`, one can check the external adress.  Done!
