# A Speech Act Analysis of Offensive Language in German Tweets

This repository provides an annotated dataset which constitutes a subset of 600 tweets taken from the dataset by Struß, Siegel, Ruppenhofer, Wiegand, and Klenner (2019) that consists of German offensive and non-offensive language tweets. The annotated dataset comprises three levels of annotation, namely coarse-grained speech acts, fine-grained speech acts and sentence types. 

From each of the six classes (implicit, explicit, profanity, insult, abuse, other), 100 tweets were randomly collected. For the two classes implicit and explicit, the 2019 gold standard files of the test data of subtask 3 were used and for the other four classes, the 2019 gold standard files of the test data from subtask 1 & 2 were used. For both test datasets, the data was shuffled using the random package from python and for each class, the first 100 occurrences were selected. Every tweet was saved as a text file which was named after the following scheme: [dataSource]“\_Tweet\_”[idNew]“\_”[idOld]“\_”[offensiveCategory]“.txt” (example: ‘s3\_Tweet\_99\_731\_implicit.txt’). Due to an error, eleven tweets had to be removed and replaced with new tweets. They were taken from the remaining set of randomly selected tweets. As an annotation tool, the open source tool INCEpTION (Klie, Bugert, Boullosa, de Castilho, & Gurevych, 2018) was chosen.

- [Link](https://projects.fzai.h-da.de/iggsa/wp-content/uploads/2019/08/germeval2019GoldLabelsSubtask1_2.txt) to original data from subtask 1 & 2
- [Link](https://projects.fzai.h-da.de/iggsa/wp-content/uploads/2019/08/germeval2019GoldLabelsSubtask3.txt) to original data from subtask 3 


## Dataset 

The dataset is available in different formats: JSON, XML and the original downloaded version from [INCEpTION](https://inception-project.github.io/). The data is located in the directory data/ .

### JSON

The file data.json contains all 600 annotated tweets in the following format:

```
{
    "s1-2_Tweet_100_1258_other.xml": {
        "tweet": {
            "scount": 2,
            "sentences": {
                "1": {
                    "stype": "ment",
                    "coarse": "DIRECTIVE",
                    "fine": "ADDRESS"
                },
                "2": {
                    "stype": "frag",
                    "coarse": "UNSURE",
                    "fine": "UNSURE"
                }
            }
        }
    }, 
    ....

```


They were transformed into this format to count occurrences for a statistical analysis.

### XML

The zipped file `data_annotated_complete.tar.gz` contains all 600 annotated XML files. 

### Original

- [Speech+Act+Analysis_curated_documents_2021-10-03_1232.zip](https://github.com/MelinaPl/speech_act_analysis/blob/main/data/Speech%2BAct%2BAnalysis_curated_documents_2021-10-03_1232.zip)

    - contains the original download format of 589 annotated Tweets (annotations in XML)

- [Speech+Act+Analysis+PII_curated_documents_2021-10-03_1645.zip](https://github.com/MelinaPl/speech_act_analysis/blob/main/data/Speech%2BAct%2BAnalysis%2BPII_curated_documents_2021-10-03_1645.zip)

    - contains the original download format of 11 annotated Tweets that were annotated seperately due to an error (annotations in XML)

## Code

All files can be found in [src/](https://github.com/MelinaPl/speech-act-analysis/tree/main/src)

- `process.py`: shows how the data from the GermEval shared task was processed
- `statistics.py`: shows examples of how the data was retrieved for the statistical analysis
- `process_annotations.py`: shows how the annotations were processed 


## Annotations

The subsequent annotation scheme is mainly inspired by Searle (1979) and Compagno et al. (2018) with regard to the speech act level. Furthermore, the idea from combining speech acts with syntactical categories is influenced by Weisser (2018). The sentence types are based on the sentence types used in the Georgetown University Multilayer Corpus (Zeldes, 2017) and contain eleven types in total. These categories are based on Leech, McEnery, and Weisser (2003) which explains the great similarity between the sentence types used in the works by Zeldes (2017) and Weisser (2018). 

The following examples are all taken from the data except for the example of the class *Accept* (marked with an asterisk)

- [Link](https://corpling.uis.georgetown.edu/wiki/doku.php?id=gum:tokenization_segmentation) to the documentation of the Georgetown University Multilayer Corpus 
- [Link](https://github.com/amir-zeldes/gum) to the Github repository of the Georgetown University Multilayer Corpus (Zeldes, 2017)

### Speech Acts

Coarse-grained | Fine-grained | Examples |
| ----------- | ----------- | ----------- | 
Assertive | Assert | “Genderstudies stehen in ihrer 20 jährigen Existenz stärker im Konflikt mit den existierenden Wissenschaften als alles davor.” | 
| | Sustain  | “Er geht mir ziemlich auf den Keks, aber wegen Vorstehendem habe ich ihn noch nicht einfach geblockt!” | 
 |  | Guess  | “Möglicherweise bin ich der Einzige, der den heterosexuellen Mann vor dem Feminismus retten kann.” | 
 |  Predict  | “Da wird mal wieder stark Übertrieben, es werden paar hundert wenn es hoch kommt | 
 |  | Agree |  “@_a_c_a_t_ das ist ein punkt, stimmt.” | 
  | | Disagree  | “@AcarLukas @allesevolution ...Dem Fehlschluss dass eine These bewiesen ist, wenn sie nicht zu 100% entkräftet werden kann. \|LBR\| Leider funktioniert das nicht so.”
 Expressive  | Rejoice  | “gut dass es #ORF gibt” | 
  | | Complain |  “Selten son Dreck im Fernsehen gesehen wie diese #krone18” | 
  | | Wish  | “Schönen Freitag.” | 
 | |  Apologize  | “btw sorry ob meiner polemik im ausgangstweet” | 
 |  | Thank  | “Danke für die Aufklärung”  | 
 |  | expressEmoji  | “:upside_down_face:” | 
Directive  | Require  | “Schämen Sie sich.” | 
 | |  Request  | “Warum veröffentlicht ihr keine Bilder von linken Anarchisten?” | 
 |  | Suggest  | “Die linke,deutsch/islamische #Bundesregierung kann den #korantreuen #Moslems #IS #Hamas doch gleich den Schlüssel zu Deutschland überreichen.” | 
 |  | Greet  | “Hallo liebe Freunde des deutschen Handballsports” | 
 |  | Address  | “@DanielDOrville2 @jogginghosenafa” | 
Commissive |  Engage |  “Ich gehe jetzt pennen.” | 
 |  | Accept*  | “Ja, das kann ich für dich machen” | 
 |  | Refuse  | “Ein echter Mann und echte Kinder? Gott behüte.” | 
 |  | Threat  |  “euch zeigen wir noch wo es lang geht.” | 
Other  | Other | “‘Die Kolonialisierung der Studentenhirne - Lyzis Welt über 40 Jahre kritische Poptheorie’”, “#Migrationsbericht” | 
Unsure  | Unsure |  “@Snakecleaver @Metalwilli OK.....!” | 


### Sentence Types 

Sentence Types | Description | Examples |
| ----------- | ----------- | ----------- | 
Declarative  |  Declarative sentence (only indicative) | “Ich hatte allerdings mit mehr Demonstranten gerechnet” | 
Exclamative  | Exclamative sentence  | “Wir schaffen das!” | 
Imperative  | Finite verb needs to be in imperative mood | “Glaubt nicht ihre Lügen” | 
Conjunctive  |  Finite verb is in conjunctive mood | “Man könnte den Islam auch verlassen.” | 
Yes-/No-Question | A question which can be answered with “yes” or “no” |  “Stimmt das?” | 
Alternative Question  | Questions asking the addressee to decide for one option | “Wie lange geht so ein Handballspiel? Zwei, drei Stunden?” | 
W-Question  | Questions formed with w-phrases | “Wie zerstört man am effektivsten die Zukunft eines Landes?” | 
Interjection  | Short exclamations, annotated if they form a sentence on their own | “Hahaha!”, “Pfui.” | 
Multiple  | Combination of two or more types due to the conjunction of two main clauses | “@poothverona sieht mit ihrem Schlauchboot im Gesicht nur noch richtig scheiße aus und sollte besser nur noch zu Halloween auftreten” | 
Other  | Sentence types not fitting in other categories (e.g. using English phrases/ sentences, constructions with “:”)  | “same bruder”, “Der Bauch sagt: hau raus,das passt schon.”, “Kalter Winter = Klimawandel” | 
Fragment |  Containing an ellipsis/ no subject predicate structure/ finite verb  | “Echtes Kunststück, dass sich da nicht ausnahmslos jeder verarscht fühlt.” | 
Non-textual  | Non-textual units such as symbols and emojis  | “:-D”, “:pray:”, “:joy:” | 
Mention |  Mentioning a person/ another twitter account, only annotated if not part of a sentence | “@mariebreizh56 @QueeniePi” | 
Hashtag |  Initial #, only annotated if not part of a sentence | “#CDUbpt18” | 

## References

Compagno, D., Epure, E., Deneckere, R., & Salinesi, C. (2018). Exploring
Digital Conversation Corpora with Process Mining. Corpus Pragmatics,
2, 193–215. doi: 10.1007/s41701-018-0030-6

Klie, J.-C., Bugert, M., Boullosa, B., de Castilho, R. E., & Gurevych, I. (2018,
Juni). The INCEpTION Platform: Machine-Assisted and Knowledge-
Oriented Interactive Annotation. In Proceedings of the 27th International
Conference on Computational Linguistics: System Demonstrations (pp.
5–9). Santa Fe, New Mexico: Association for Computational Linguistics.
Retrieved from https://aclanthology.org/C18-2002

Leech, G., McEnery, T., & Weisser, M. (2003). SPAAC Speech-Act Annotation
Scheme. University of Lancaster, Technical Report.

Struß, J. M., Siegel, M., Ruppenhofer, J., Wiegand, M., & Klenner, M. (2019).
Overview of GermEval Task 2, 2019 Shared Task on the Identification
of Offensive Language. In German Society for Computational Linguis-
tics. Proceedings of the 15th Conference on Natural Language Processing
(KONVENS) 2019 (pp. 354–365). Nürnberg/Erlangen.

Weisser, M. (2018). How to Do Corpus Pragmatics on Pragmatically Anno-
tated Data: Speech Acts and Beyond. Amsterdam/Philadelphia: John
Benjamins Publishing Company. doi: 10.1075/scl.84

Zeldes, A. (2017). The GUM Corpus: Creating Multilayer Resources in the
Classroom. Language Resources and Evaluation, 51(3), 581–612. doi:
10.1007/s10579-016-9343-x
