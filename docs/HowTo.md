# Mon site DIY ?

Parce que je ne suis pas un informaticien de formation, la réalisation de ces pages internet aura été un peu fastidieuse. Néanmoins, avec l'aide de mes camarades de jeu à l'ESRF, j'ai compris 2/3 bricoles (HMTL/CSS/javascript et le générateur statique de site). Et j'ai finalement - enfin! - trouvé le [tuto YT](https://www.youtube.com/watch?v=Q-YA_dA8C20) qui sauve la vie.
See also the [documentation page](https://squidfunk.github.io/mkdocs-material/reference/images/) of the `material-for-mkdoc` theme.

## Quelques éléments de vocabulaire

La recette qui suit n'est pas accessible à tout le monde. Il faut quelques connaissances `python`, `github`, `mardown`... MAIS: une fois toutes ces étapes techniques réalisées, la mise à jour du site n'est pas plus compliquée que de modifier des fichiers de texte.

- `mkdoc` est le générateur statique de site. C'est une sorte de modèle de site un peu enrichi, qui lit des fichiers de texte et construit le site en interprétant ces fichiers texte et en les mettant en page.
- la mise en page est gérée par un `theme`.
- La génération du site ainsi que sa publication en ligne est faite par la plateforme `GitHub`.
- `GitHub` est une plateforme de développement informatique collaboratif.

Quelques commandes de base pour démarrer avec `mkdoc`.:
* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.


## How to?

It requires:

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

## A propos des cartes IGN et des traces.

- Pour faire les traces GPX, [GPXStudio](https://gpx.studio/) est pas mal du tout. En pointant sur des points sur les chemins identifiés sur le fonds de carte, il créé l'itinéraire. La trace GPX peut ensuite être exportée.
- Pour générer les fonds de carte, tout se fait dans le [Geoportail](https://www.geoportail.gouv.fr):
  - Avec un compte, on peut uploader les traces GPX (qui seront conservées dans le compte).
  - Les traces GPX sont alors accessibles comme fond de carte.
  - Il suffit alors de partager et insérer le bout de code HTML dans la page.
- La page, qui contient toutes les étapes, est un peu lourde à charger... A voir.
