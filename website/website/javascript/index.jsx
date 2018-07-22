import React from "react";
import { render } from "react-dom";
import Upload from "./Upload";
import Stats from "./Stats";

require("@blueprintjs/core/lib/css/blueprint.css");
require("@blueprintjs/icons/lib/css/blueprint-icons.css");

const UploadContainer = document.getElementById("react-image-upload");
if (UploadContainer) {
  render(<Upload />, UploadContainer);
}

const StatsContainer = document.getElementById("react-stats");
if (StatsContainer) {
  render(<Stats />, StatsContainer);
}
