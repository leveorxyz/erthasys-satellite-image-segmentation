import { Circle } from "@mui/icons-material";

export default function Legend() {
    return (
        <div className="Legend">
            <div className="ColorLabel">
                <Circle sx={{ color: "#3C1098" }} />
                <p> Building</p>
            </div>
            <div className="ColorLabel">
                <Circle sx={{ color: "#8429F6" }} />
                <p>Land</p>
            </div>
            <div className="ColorLabel">
                <Circle sx={{ color: "#6EC1E4" }} />
                <p>Road</p>
            </div>
            <div className="ColorLabel">
                <Circle sx={{ color: "#FEDD3A" }} />
                <p>Vegetation</p>
            </div>
            <div className="ColorLabel">
                <Circle sx={{ color: "#E2A929" }} />
                <p>Water</p>
            </div>
            <div className="ColorLabel">
                <Circle sx={{ color: "#9B9B9B" }} />
                <p>Unlabeled</p>
            </div>
        </div>
    );
}
