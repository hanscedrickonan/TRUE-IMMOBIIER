# True Immobilier — site vitrine

Rénovation, location et vente de biens immobiliers à Abidjan.
Site une page en 3D : le logo True Immobilier, en verre, s'éclate puis se recompose au scroll.

**À remplacer avant la mise en ligne :**
- l'e-mail provisoire `contact@true-immobilier.ci` dans `index.html` (attribut `data-email` du formulaire et lien `mailto:`) ;
- les trois chiffres du chapitre Résultats (`data-count="120"`, `"85"`, `"98"` dans `index.html`), qui sont des exemples.

Ensuite, lancez `python3 build_monofichier.py` pour régénérer `version-monofichier.html`.

---

# Site Premium 3D Glass

Site vitrine d'une seule page, piloté au scroll : un objet en verre optique se
décompose en quatre fragments puis se recompose à l'identique, sur cinq chapitres. Rendu en
temps réel avec Three.js, sans aucune image ni vidéo.

## Ouvrir

```sh
python3 serve.py
```

Puis <http://127.0.0.1:8000>. Un autre port : `python3 serve.py 8080`.
Le navigateur doit gérer WebGL 2, les modules JavaScript et les import maps.

`version-monofichier.html` contient tout le site dans un seul fichier et s'ouvre
directement. Régénérez-le après toute modification :

```sh
python3 build_monofichier.py
```

## Modifier

| Quoi | Où |
|---|---|
| Textes, menu, e-mail | `index.html` |
| Forme 3D | `assets/shapes/shape.svg` |
| Logo du header | `assets/brand/mark.svg` |
| Couleurs du fond | `SITE.palette` en tête de `js/app.js` |
| Taille des objets, cadrage | `LOGO_HEIGHT`, `ICON_SIZE`, `cameraFrame` dans `js/app.js` |
| Mise en page, header, formulaire | `css/styles.css` |

Nouvelle forme depuis la bibliothèque :

```sh
python3 tools/make_shape.py --list
python3 tools/make_shape.py hexagon assets/shapes/shape.svg
```

Vérifier un logo avant de l'utiliser :

```sh
python3 tools/make_shape.py --check-file mon-logo.svg
```

Tout régénérer depuis un brief JSON :

```sh
python3 tools/build_site.py site.json --out ../mon-site
```

## Formulaire

Le formulaire ouvre la messagerie du visiteur avec un message prérempli, sujet et
champs compris. Il ne dépend d'aucun serveur : le site s'héberge sur n'importe quel
hébergement statique. L'adresse se change dans `index.html`, dans l'attribut
`data-email` du formulaire et dans le lien `mailto:`.

## Contenu

```text
index.html                 Structure et contenu éditorial
css/styles.css             Mise en page, header, curseur, formulaire, préchargeur
css/fonts.css              Déclarations de Space Grotesk
js/app.js                  Scène 3D, verre, découpage, morphing, shader, scroll
assets/shapes/             La silhouette en verre
assets/brand/mark.svg      Le logo du header
assets/fonts/              Space Grotesk (300 à 700)
vendor/                    Three.js r160 et SVGLoader
tools/make_shape.py        Bibliothèque de formes et validateur de SVG
tools/build_site.py        Génère un site depuis un brief JSON
serve.py                   Petit serveur local
build_monofichier.py       Produit version-monofichier.html
licenses/                  Licences Three.js et Space Grotesk
```
