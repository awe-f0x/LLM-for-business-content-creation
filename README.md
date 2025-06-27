# 🌟 LLM-for-business-content-creation 🌟
**GitHub Repository: `LLM-for-business-content-creation`**

Within the framework of this project, an LLM is being created, which will be used to improve the quality of the Bank of Russia’s communications texts.

# Problem statement 

Among the tools that central banks use to manage inflation, communications occupy a special place: they can increase the effectiveness of monetary policy (MP). Two key characteristics of effective official communication are transparency and readability.
Transparency of communication is understood as the degree of disclosure of information about their decisions and their reasoning. Readability is defined as a set of all text parameters that help the reader quickly understand the information contained in it.
Readability and transparency are important for any central bank audience. If the central bank communicates clearly, unambiguously and fully discloses the logic of decision-making, then it is better understood by representatives of both a well-prepared audience (the financial sector, investors, analysts) and a wider public (the real sector, the population).

To measure the quality of communication, 2 metrics are used:
Readability - ARIEstimator
Transparency - AlinaEstimator
[Research describing the tools (in Russian)](https://rjmf.econs.online/2021/3/clarity-of-monetary-policy-communication/)

These metrics are quantitative, and although they allow you to effectively measure the quality of communications, they need support by expert assessment.
Therefore, we have supplemented them with criteria that experts will be guided by when giving their assessments:
1) Clarity/consistency of logical transitions within a sentence, between sentences, paragraphs.
2) Completeness/sufficiency of arguments for the conclusion.
3) Uniqueness of the logical conclusion made by the model (is it possible to make a different conclusion based on the presented facts/arguments).
4) Comparison with the source for details lost during processing that affect the final conclusion.
5) The number of arguments used that allowed the final conclusion to be made.


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

2. To get an expert assessment of the text quality, send an email to akulichevda@cbr.ru and kostornoyav@cbr.ru in the following format:
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
4. We will perform an expert assessment of the texts
5. The final assessment will contain all 3 metrics: ARIEstimator, AlinaEstimator and the assessment of the experts.
Additional points can be awarded separately by our Expert Team

