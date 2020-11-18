#  Le discret Napier


## Description

Stockos a encore choisi un code d'accès qui est solution d'une énigme mathématique ! Retrouvez x tel que : `17^x ≡ 183512102249711162422426526694763570228 [207419578609033051199924683129295125643]`

Le flag est de la forme : DGSESIEE{x} avec x la solution

## Solution

Le challenge nous demande de résoudre une équation mathématique qui à première vue est difficile à résoudre.

La première étape à été de se renseigner sur Napier, qui est un mathématicien ayant inventé les logarithmes.

Le titre de challenge nous dirige donc vers un logarithme discret.

Une recherche Google avec les mots clés "logarithme discret python" permet de trouver une [page web](https://wiki.zenk-security.com/doku.php?id=hackingweek_2014:crypto:crypto5) résolvant un problème similaire.

On utilise donc le même outils [magma](http://magma.maths.usyd.edu.au/calc/), en remplaçant par nos valeurs.

```
p:=207419578609033051199924683129295125643;
g:=17;
X:=183512102249711162422426526694763570228;

Log(GF(p)!g, GF(p)!X);
```

Le résultat est `697873717765`, il ne reste plus qu'à valider le flag `DGSESIEE{697873717765}`.