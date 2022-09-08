export default async function getSegmentedImage(b64Image) {
    const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: b64Image }),
    };

    const response = await fetch("/erthasys", requestOptions);
    const data = await response.json();

    return [data.prediction, data.class_distribution];
}
