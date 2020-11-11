# Pivot-for-Low-Resource-Languges
This repository describes our works in Word Reordering on Multiple Pivots for the Japanese and Indonesian Language Pair 

## Extended phrase table
We employed an extending phrase table to minimize the Japanese UNK in the source-pivot (src-pvt) system. The extending phrase table used two types of symmetrization: *grow-diag-final-and* and *tgttosrc*. We assumed that two phrase tables of Ja-En were available by using two types of symmetrization, namely, the Ja-En phrase table of *grow-diag-final-and* as T<sub>gdfand</sub> and Ja-En phrase table of *tgttosrc* as T<sub>tgttosrc</sub>. Each phrase table has four translation parameters, namely, the phrase translation probabilities for both directions, that is, (t|s) and (s|t), and lexical translation probabilities for both directions, that is (t|s), and (s|t). First, we sorted the Japanese UNK of the src-pvt system as Condition (C). Then, we searched candidate pairs of C in the phrase table of *tgttosrc* as T<sub>filtered</sub>. Finally, we merged the two phrase tables of T<sub>gdfand</sub> and T<sub>filtered</sub>. 

### Input files
```
  Generated text of translation system, example:
  00-1a-DataALT.03.Testing.1K.translated.detoken.gdfand.JaEn
  
```

### Running codes

```
  python3 nihonggofinder.py > 00-1b-DataALT.03.ja-id.OOV.gdfand.JaEn
  python3 jpnsorter.py > 00-1c-DataALT.03.ja-id.sortedOOV.gdfand.JaEn

```
