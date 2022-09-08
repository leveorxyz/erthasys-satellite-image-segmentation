import { useState } from "react";

import Legend from "./components/Legend";
import ImageUpload from "./components/ImageUpload";
import getSegmentedImage from "./api/erthasys";
import convertBase64 from "./utils/base64utils";

import "./App.css";

function App() {
    const [inputImage, setInputImage] = useState(null);
    const [predictedImage, setPredictedImage] = useState(null);
    const [classDistribution, setClassDistribution] = useState("");

    const processInputImage = async (image) => {
        setPredictedImage(null);
        setClassDistribution("");
        const b64Image = await convertBase64(image);
        setInputImage(b64Image);
        const [prediction, classDistribution] = await getSegmentedImage(
            b64Image
        );
        console.log(classDistribution);
        setPredictedImage(prediction);
        setClassDistribution(JSON.stringify(classDistribution));
    };

    return (
        <div className="App">
            <Legend />
            <div className="Images">
                {inputImage && <img src={inputImage} alt="input" width={512} />}
                {predictedImage && (
                    <img src={predictedImage} alt="prediction" width={512} />
                )}
            </div>
            <ImageUpload onFinishUpload={processInputImage} />
            <p>{classDistribution}</p>
        </div>
    );
}

export default App;
