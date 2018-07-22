import React from "react";
import { render } from "react-dom";
// import SubjectSearch from './SubjectSearch'
// import CourseSearch from './CourseSearch'
import FAQs from "./FAQs";
import Upload from "./Upload";
import Stats from "./Stats";
import { Intent, Spinner } from "@blueprintjs/core";

require("@blueprintjs/core/lib/css/blueprint.css");
require("@blueprintjs/icons/lib/css/blueprint-icons.css");

// const SubjectSearchContainer = document.getElementById('react-subject-search')
// if (SubjectSearchContainer) {
//   render(<SubjectSearch />, SubjectSearchContainer)
// }
//
// const CourseSearchContainer = document.getElementById('react-course-search')
// if (CourseSearchContainer) {
//   render(<CourseSearch />, CourseSearchContainer)
// }
//

const UploadContainer = document.getElementById("react-image-upload");
if (UploadContainer) {
  render(<Upload />, UploadContainer);
}

const StatsContainer = document.getElementById("react-stats");
if (StatsContainer) {
  render(<Stats />, StatsContainer);
}

// ReactDOM.render(
//   <Spinner intent={Intent.PRIMARY} />,
//   document.getElementById('react-spinner')
// )
