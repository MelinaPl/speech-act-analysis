# A Speech Act Analysis of Offensive Language in German Tweets

This repository provides an annotated dataset which constitutes a subset of 600 tweets taken from the dataset by Struß, Siegel, Ruppenhofer, Wiegand, and Klenner (2019) that consists of German offensive and non-offensive language tweets. The annotated dataset comprises three levels of annotation, namely coarse-grained speech acts, fine-grained speech acts and sentence types. 

From each of the six classes (implicit, explicit, profanity, insult, abuse, other), 100 tweets were randomly collected. For the two classes implicit and explicit, the 2019 gold standard files of the test data of subtask 3 were used 12 and for the other four classes, the 2019 gold standard files of the test data from subtask 1 & 2 were used. For both test datasets, the data was shuffled using the random package from python and for each class, the first 100 occurrences were selected. Every tweet was saved as a text file which was named after the following scheme: [dataSource]“_Tweet_”[idNew]“_”[idOld]“_”[offensiveCategory]“.txt” (example: ‘s3_Tweet_99_731_implicit.txt’). Due to an error, eleven tweets had to be removed and replaced with new tweets. They were taken from the remaining set of randomly selected tweets. As an annotation tool, the open source tool INCEpTION14 (Klie, Bugert, Boullosa, de Castilho, & Gurevych, 2018) was chosen.

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

## References

Klie, J.-C., Bugert, M., Boullosa, B., de Castilho, R. E., & Gurevych, I. (2018,
Juni). The INCEpTION Platform: Machine-Assisted and Knowledge-
Oriented Interactive Annotation. In Proceedings of the 27th International
Conference on Computational Linguistics: System Demonstrations (pp.
5–9). Santa Fe, New Mexico: Association for Computational Linguistics.
Retrieved from https://aclanthology.org/C18-2002

Struß, J. M., Siegel, M., Ruppenhofer, J., Wiegand, M., & Klenner, M. (2019).
Overview of GermEval Task 2, 2019 Shared Task on the Identification
of Offensive Language. In German Society for Computational Linguis-
tics. Proceedings of the 15th Conference on Natural Language Processing
(KONVENS) 2019 (pp. 354–365). Nürnberg/Erlangen.
