# Dataset Version 1.1

The dataset is currently only available in JSON format. It is availabe [here](https://github.com/MelinaPl/speech-act-analysis/blob/main/data/version_1-1.json).

## Changes Compared to Previous Version

The previous dataset version contained two main error types. The first error concerns the text spans which sometimes have been cut off at the end or the beginning. This, however, does not influence the number of speech acts in the dataset. The second error influences the number of speech acts, as some speech acts have been missing due to an error in my processing script as well as due to an error regarding previously unannotated data. In total, 35 speech acts have been added in version 1.1. This raises the number of speech acts from 1924 to 1959 in version 1.1.

### Text Spans

Affected tweets:

-   s1-2_Tweet_45_805_other
-   s1-2_Tweet_103_2837_other
-   s1-2_Tweet_657_2855_insult
-   s1-2_Tweet_145_130_abuse
-   s1-2_Tweet_476_2532_profanity
-   s1-2_Tweet_780_148_abuse
-   s1-2_Tweet_236_827_abuse
-   s1-2_Tweet_395_2848_profanity
-   s1-2_Tweet_66_279_abuse
-   s1-2_Tweet_199_878_abuse
-   s1-2_Tweet_479_839_abuse
-   s1-2_Tweet_34_824_abuse
-   s3_Tweet_109_412_explicit
-   s1-2_Tweet_107_2498_other
-   s1-2_Tweet_39_147_other
-   s1-2_Tweet_253_2881_abuse
-   s1-2_Tweet_510_221_abuse
-   s1-2_Tweet_2052_152_profanity
-   s3_Tweet_13_518_implicit
-   s1-2_Tweet_519_299_abuse
-   s1-2_Tweet_8_2570_insult
-   s1-2_Tweet_128_2518_other
-   s3_Tweet_110_138_explicit
-   s1-2_Tweet_147_1814_abuse
-   s1-2_Tweet_87_404_other


### Additional Speech Acts

#### Missing Annotation in XML File

Affected tweets: 

-	s1-2_Tweet_601_2524_abuse.xml: sentence 2
-	s1-2_Tweet_665_778_profanity: sentence 2 and 3
-	s3_Tweet_2_82_explicit: sentence 3
-	s3_Tweet_18_130_explicit: sentence 3
-	s1-2_Tweet_65_2699_other: sentence 2
-	s1-2_Tweet_319_850_insult: sentence 2
-	s3_Tweet_95_216_explicit: sentence 4
-	s1-2_Tweet_369_808_insult: sentence 2
-	s1-2_Tweet_538_2485_abuse: sentence 4
-	s3_Tweet_108_325_explicit: sentence 3
-	s1-2_Tweet_518_875_abuse: sentence 2 and 3
-	s1-2_Tweet_144_57_abuse: sentence 2 and 3 
-	s3_Tweet_83_190_explicit: sentence 2
-	s1-2_Tweet_485_854_abuse: sentence 2 and 3
-   s1-2_Tweet_104_1481_other: sentence 3
-   s1-2_Tweet_137_1381_insult: sentence 7
-   s3_Tweet_32_416_explicit: sentence 3


#### Error in Script

- Wrong iteration in my python script lead to 14 missing speech acts (fixed)

### Fixed Annotation Mistakes

-	s1-2_Tweet_780_148_abuse: character „6“ was not in annotation span, corrected manually
-	s3_Tweet_11_895_explicit: character „n” at the end was not in annotation span, corrected manually
-	s3_Tweet_77_713_explicit: last character „i“ in "Polizei" was not in annotation span, corrected manually

## Updated Statistics

Coming soon
