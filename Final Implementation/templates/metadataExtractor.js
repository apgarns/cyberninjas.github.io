async function extractMetadata() {
    const fileInput = this.document.getElementById("input-file");
    const metadataDisplay = this.document.getElementById("metadata-display");
    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a file to extract metadata");
        return;
    }
    try {
        const fileReader = new FileReader();
        const fileDataPromise = new Promise((resolve, reject) => {
            fileReader.onload = (event) => {
                resolve(event.target.result);
            };
            fileReader.onerror = () => {
                reject("Error reading file");
            };
        });
        fileReader.readAsArrayBuffer(file);
        const fileData = await fileDataPromise;
        const metadata = await exifr.parse(fileData);
        metadataDisplay.innerHTML = JSON.stringify(metadata, null, 2);
    } catch (error) {
        console.log("Error extracting metadata:", error);
        metadataDisplay.innerHTML = "Error extracting metadata";
    }
}

function initMetadataExtractor() {
    const extractMetadataButton = this.document.getElementById("extract-metadata");
    if (extractMetadataButton) {
        extractMetadataButton.addEventListener("click", extractMetadata.bind(this));
    }
}

window.onload = initMetadataExtractor;