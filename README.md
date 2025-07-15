# 🌟 LLM-for-business-content-creation 🌟
**GitHub Repository: `LLM-for-business-content-creation`**

Within the framework of this project, an LLM is being created, which will be used to improve the quality of the Bank of Russia’s communications.

# Problem statement 

Quality communications are crucial for any central bank. If a regulator communicates clearly, unambiguously and fully discloses the logic behind its decisions, its strategy is better understood by both professional community (such as financial experts, investors, analysts) and wider public (real sector and ordinary citizens).
Clear official communications positively impact inflation expectations and increase overall trust to the Central Bank’s and other Ministries’ decisions leading countries to economic growth and prosperity.
While nowadays most texts are created by humans – Natural Intelligence – who often tend to complex narrative full of professional terms, we would like to use AI to clarify and shorten them without distorting storyline or losing important details.

In this context, we suggest you to design and deploy an LLM, which will process texts on banking regulation and analytics in order to boost their transparency and readability:
·         Transparency of communication is the degree of disclosure of information on the Regulator’s decisions and the underlying reasoning.
·         Readability is a set of multiple text parameters helping the audience quickly understand the information contained.

To measure the quality of the resulting communication we will use two metrics:
·         For transparency – AlinaEstimator, that uses syntaxes’, lexical, morphology, phonetic, semantic and some other text characteristics.
·         For readability – ARIEstimator that is based on the well-known FRE (Flesch Reading Ease) readability metrics.

[Research describing the tools (in Russian)](https://rjmf.econs.online/2021/3/clarity-of-monetary-policy-communication/)

These are quantitative metrics which allow measurement of the overall quality of communications. To ensure that the resulting texts comply with the non-quantitative criteria, they should also pass an expert assessment.
Below are the key non-quantitative criteria to backbone the expert assessment:
1) Clarity / consistency of logical transitions within a sentence, between sentences, paragraphs.
2) Completeness / sufficiency of arguments for the conclusion.
3) Uniqueness of the logical conclusions made by LLM (is it possible to make a different conclusion based on the presented facts / arguments).
4) Loss of crucial details (against source text) impacting the final conclusion.


## 🎯 Objective

**Train an LLM** that will improve the quality of source texts without violating expert criteria.

---


## 📁 Project Structure

```bash
LLM-for-business-content-creation/main/
├── README.md                      # This file
├── data/
│   └── dataset.json               # Dataset for LLM training
└── examples/
    └── text_evaluation.py         # API-usage example
```

## 📥 Input Data Format

An example input:

```json
{
  "guid": "5244e629-13fb-45f1-ad58-15a2bf3472b4",
  "ARIEstimator": 1.8929999999999967,
  "AlinaEstimator": 6.0,
  "text": "Здесь находится текст на русском языке размером от 100 до 400 символов в формате utf-8",
  "words_count": 158
}
```

Several texts contain the Error mark for the AlinaEstimator metric - to obtain a numerical score for this metric, their **content must be shortened** without losing meaning.

---

## 🛠️ Tools & Libraries

- `requests` – API calls
- `transformers` – LLM interaction

---

## 📊 Evaluation Process

1. To get an assessment based on ARIEstimator and AlinaEstimator text metrics, use the [Swagger](http://skolkovo.cbrai.ru/docs) verifier API
Limitations: 
- no more than 400 words in one text fragment
- no more than 100 requests per hour

2. To get an expert assessment of the text quality, send an email to dimaakulichev@yandex.ru and small-horse@yandex.ru in the following format:
- guid of the original text
- original text
- processed text
Limitation: no more than 5 texts per day

---

## 🧠 Suggested LLM Models

> Use any you find most suitable

---

## 📚 Validation Dataset

We will provide a validation dataset consisting of 5 texts before the end of the summer school.

---

## 🙋 Contributors

Feel free to submit PRs or open issues. This project is designed to grow beyond the summer school!

---

## 🏷 License

MIT License

---

## ✅ Validation

1. We will install your model - it should not have any errors during installation
2. We will run it in real time to improve the quality of the texts validation dataset
3. We will receive assessments of the improved texts by ARIEstimator and AlinaEstimator
4. We will perform expert assessment of the resulting texts
5. The final assessment will contain all 3 metrics: ARIEstimator, AlinaEstimator and expert assessment.
Extra points can be awarded separately by the expert team for exceptional narrative style and client-ready solutions.

For questions or clarifications, please contact your project mentors (telegram: [Dmitriy Bazyukin](https://t.me/DmBzzz), [Andrey Kostornoy](https://t.me/awe_fox))

