const form = document.getElementById("predictionForm");
const button = document.getElementById("predictButton");

const loading = document.getElementById("loading");
const error = document.getElementById("error");
const result = document.getElementById("result");

const riskElement = document.getElementById("risk");
const confidenceElement = document.getElementById("confidence");
const probabilityElement = document.getElementById("probability");

form.addEventListener("submit", async (event) => {

    event.preventDefault();

    loading.classList.remove("hidden");
    error.classList.add("hidden");
    result.classList.add("hidden");

    button.disabled = true;
    button.textContent = "Predicting...";

    const payload = {
        attendance: Number(document.getElementById("attendance").value),
        assignments_completed: Number(
            document.getElementById("assignments").value
        ),
        exam_score: Number(document.getElementById("exam").value),
        engagement_score: Number(
            document.getElementById("engagement").value
        )
    };

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Prediction failed.");
        }

        const risk = data.dropout_risk;

        riskElement.textContent = `${risk.toUpperCase()} RISK`;
        confidenceElement.textContent =
            `${(data.confidence * 100).toFixed(1)}%`;

        probabilityElement.textContent =
            `${(data.risk_probability * 100).toFixed(1)}%`;

        result.classList.remove("hidden");

    } catch (err) {

        error.textContent = err.message;
        error.classList.remove("hidden");

    } finally {

        loading.classList.add("hidden");
        button.disabled = false;
        button.textContent = "Predict Dropout Risk";

    }
});