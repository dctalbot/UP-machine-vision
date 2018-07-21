import React from "react";
import styled from "styled-components";

import { RadioGroup, Radio } from "@blueprintjs/core";

// require("@blueprintjs/core/lib/css/blueprint.css")
// require("@blueprintjs/icons/lib/css/blueprint-icons.css")

const Container = styled.div`
  text-align: center;
`;

const List = styled.ul`
  text-align: left;
`;

export default class FAQs extends React.Component {
  render() {
    return (
      <Container>
        <RadioGroup
          label="Meal Choice"
          onChange={alert("hi")}
          selectedValue={"this.state.mealType"}
        >
          <Radio label="Soup" value="one" />
          <Radio label="Salad" value="two" />
          <Radio label="Sandwich" value="three" />
        </RadioGroup>

        <h3>Frequently Ased Questions</h3>
        <List>
          <li>Have we got any Nickleback fans in Portugal?</li>
          <li>React is fun!</li>
          <li>Styled components are awesome:D</li>
          <li>Each question could be a click to expand sort of thing</li>
        </List>
      </Container>
    );
  }
}
