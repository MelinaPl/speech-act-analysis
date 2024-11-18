# A Speech Act Analysis of Offensive Language in German Tweets

This repository provides an annotated dataset which constitutes a subset of 600 tweets taken from the dataset by Struß, Siegel, Ruppenhofer, Wiegand, and Klenner (2019) that consists of German offensive and non-offensive language tweets. The annotated dataset comprises three levels of annotation, namely coarse-grained speech acts, fine-grained speech acts and sentence types. 

From each of the six classes (implicit, explicit, profanity, insult, abuse, other), 100 tweets were randomly collected. For the two classes implicit and explicit, the 2019 gold standard files of the test data of subtask 3 were used and for the other four classes, the 2019 gold standard files of the test data from subtask 1 & 2 were used. For both test datasets, the data was shuffled using the random package from python and for each class, the first 100 occurrences were selected. Every tweet was saved as a text file which was named after the following scheme: [dataSource]“\_Tweet\_”[idNew]“\_”[idOld]“\_”[offensiveCategory]“.txt” (example: ‘s3\_Tweet\_99\_731\_implicit.txt’). Due to an error, eleven tweets had to be removed and replaced with new tweets. They were taken from the remaining set of randomly selected tweets. As an annotation tool, the open source tool INCEpTION (Klie, Bugert, Boullosa, de Castilho, & Gurevych, 2018) was chosen.

## Note: New Version (1.1) Available (Fixed Bugs)

13.10.2023: Upload of new version 1.1 of the dataset which contain bug fixes.

Dataset available [here](https://github.com/MelinaPl/speech-act-analysis/blob/main/data/version_1-1.json)

For a documentation of the changes, see document [version_1-1_changes.md](https://github.com/MelinaPl/speech-act-analysis/blob/main/version_1-1_changes.md). Version 1.1 is only available in JSON format. Please do not use the old version as it contains some bugs that have been fixed in version 1.1.

## Dataset 

The dataset is available in different formats: JSON, XML and the original downloaded version from [INCEpTION](https://inception-project.github.io/). The data is located in the directory data/ .

### JSON

There are two types of JSON files available for download: 

- [annotations_without_text.json](https://github.com/MelinaPl/speech-act-analysis/blob/main/data/annotations_without_text.json)
- [annotations_with_text.json](https://github.com/MelinaPl/speech-act-analysis/blob/main/data/annotations_with_text.json)

The files each contain all 600 annotated tweets in the following format:

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


### XML

The zipped file `data_annotated_complete.tar.gz` contains all 600 annotated XML files. 

## Code

All files can be found in src/

- `process.py`: shows how the data from the GermEval shared task was processed
- `statistics.py`: shows examples of how the data was retrieved for the statistical analysis
- `process_annotations.py`: shows how the annotations were processed 


## Annotations

The subsequent annotation scheme is mainly inspired by Searle (1979) and Compagno et al. (2018) with regard to the speech act level. Furthermore, the idea from combining speech acts with syntactical categories is influenced by Weisser (2018). The sentence types are based on the sentence types used in the Georgetown University Multilayer Corpus (Zeldes, 2017) and contain eleven types in total. These categories are based on Leech, McEnery, and Weisser (2003) which explains the great similarity between the sentence types used in the works by Zeldes (2017) and Weisser (2018). 

The following examples are all taken from the data except for the example of the class *Accept* (marked with an asterisk)

- [Link](https://wiki.gucorpling.org/gum/tokenization_segmentation) to the documentation of the Georgetown University Multilayer Corpus 
- [Link](https://github.com/amir-zeldes/gum) to the Github repository of the Georgetown University Multilayer Corpus (Zeldes, 2017)

### Speech Acts

#### Speech Acts

- **Assertive**: Assert, Sustain, Guess, Predict, Agree, Disagree
- **Expressive**: Rejoice, Complain, Wish, Apologize, Thank, expressEmoji
- **Directive**: Require, Request, Suggest, Greet, Address 
- **Commissive**: Engage, Accept, Refuse, Threat
- **Unsure**: Unsure
- **Other**: Other 

| Speech Acts | Description | Examples |
| ----------- | ----------- | ----------- | 
| Assert | To assert something. | "Genderstudies sthene in ihrer 20 jährigen Existenz stärker im Konflikt mit den existierenden Wissenschaften als alles davor.|
| Sustain | To sustain an assertion with arguments. | Mittlerweile werden deutsche Frauen die Hilfe brauchen abgewiesen, weil nicht genug Plätze vorhanden sind.|
| Guess | To weaken an assertion by introducing probability/possibility of the assertion. | Möglicherweise bin ich der Einzige, der den heterosexuellen Mann vor dem Feminismus retten kann. |
| Predict | An assertion that refers to the future. | "es werden paar hundert wenn es hoch kommt"|
| Agree | Agreeing with something/someone. | "das ist ein punkt, stimmt."|
| Disagree | Disagreeing with something/someone. | (begin context) *@AcarLukas @allesevolution ...Dem Fehlschluss dass eine These bewiesen ist, wenn sie nicht zu 10\% entkräftet werden kann.* (end context) "\|LBR\| Leider funktioniert das nicht so." |
| Rejoice | Expressing a positive attitude towards someone/something. | "gut dass es #ORF gibt" |
| Complain | To complain, e.g., expressing a negative attitude towards something/someone. | "Selten son Dreck im Fernsehen gesehen wie diese #krone18" |
| Wish | Wishing for something. | "Schönen Freitag." |
| Apologize | Apologizing to someone for something. | "btw sorry ob meiner polemik im ausgangstweet" |
| Thank | Thanking someone. | "Danke für die Aufklärung" |
| expressEmoji | Used for an emoji or series of emojis. | "🙃" |
| Require | (Strongly) requiring someone to do something. Usually used for commands. | "Schämen Sie sich." |
| Request | Requesting someone to do something. Usually used for questions. | "Warum veröffentlicht ihr keine Bilder von linken Anarchisten?" |
| Suggest | Suggesting something to someone. Can be used positively or negatively. | Die linke,deutsch/islamische #Bundesregierung kann den #korantreuen #Moslems #IS #Hamas doch gleich den Schlüssel zu Deutschland überreichen" |
| Greet | Greeting someone. | "Hallo liebe Freunde des deutschen Handballsports" |
| Address | Addressing someone. Used for mentions (@xyz). | "@DanielDOrville2 @jogginghosenafa" |
| Engage | Committing oneself to do something. | "Ich gehe jetzt pennen." |
| Accept* | Accepting something based on a previous utterance. | "Ja, das kann ich für dich machen" |
| Refuse | Refusing something based on a previous utterance. | (begin context) *Ein echter Mann und echte Kinder?* (end context) "Gott behüte" |
| Threat | Threatening someone. | "euch zeigen wir noch wo es lang geht." |
| Unsure | Used when an utterance in a tweet cannot be classified due to missing or insufficient context. | (begin context) *@Snakecleaver @Metalwilli* (end context) "OK.....!" |
| Other | Used for speech acts not represented in this annotation scheme. | "#Migrationsbericht" |


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

Austin, J. L. (1962). How to Do Things with Words. Oxford University Press.

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

Searle, J. R. (1979). Expression and Meaning: Studies in the Theory of Speech Acts. Cambridge University
Press, Cambridge.

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

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
