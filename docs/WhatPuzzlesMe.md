title: This page mixes encrypted and normal content
level: secret
inject_id: protected
delete_id: teaser

# Test
<iframe
  src="https://www.lemonde.fr/idees/article/2023/11/26/pour-la-premiere-fois-toute-l-union-europeenne-a-enclenche-la-marche-arriere-sur-l-environnement_6202428_3232.html"
  width="100%"
  height="500"
  frameborder="0"
  allowfullscreen
  sandbox>
  <p>
    <a href="https://www.lemonde.fr/idees/article/2023/11/26/pour-la-premiere-fois-toute-l-union-europeenne-a-enclenche-la-marche-arriere-sur-l-environnement_6202428_3232.html">
      Lien de repli pour les navigateurs ne prenant pas en charge iframe
    </a>
  </p>
</iframe>


/// html | div#teaser
## Teaser

You won't believe which secrets this page will unveil.
Find out more after you enter the correct password...
///

/// html | div#protected
## Secret

Well, the princess is another castle.
///