import { Button } from "@mui/material";
import { CloudUpload } from "@mui/icons-material";

export default function ImageUpload({ onFinishUpload }) {
    return (
        <div className="ImageUpload">
            <input
                accept="image/*"
                className="SelectImage"
                style={{ display: "none" }}
                id="raised-button-file"
                multiple
                type="file"
                onChange={(event) => {
                    const image = event.target.files[0];
                    onFinishUpload(image);
                }}
            />
            <label htmlFor="raised-button-file">
                <Button
                    variant="contained"
                    component="span"
                    className="UploadButton"
                    size="large"
                    startIcon={<CloudUpload />}
                >
                    Upload Image
                </Button>
            </label>
        </div>
    );
}
