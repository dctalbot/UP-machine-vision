import React from "react";
import styled from "styled-components";

import { RadioGroup, Radio, Button, MenuItem, FormGroup, FileInput } from "@blueprintjs/core";
import { Select } from "@blueprintjs/select";
import { Pie } from "react-chartjs-2";

const Container = styled.div`
  text-align: center;
`;

export default class Stats extends React.Component {
  constructor() {
    super();

    this.state = {
      normal: 0,
      broken: 0
    };
  }

  componentDidMount() {
    console.log("mounted");
    const n = document.getElementById("normal_pct").value;
    const b = document.getElementById("broken_pct").value;
    const nl = document.getElementById("normal_label").value;
    const bl = document.getElementById("broken_label").value;
    this.setState({
      normal: n,
      broken: b,
      nl: nl,
      bl: bl
    });
  }

  render() {
    return (
      <Container>
        <Pie
          data={{
            datasets: [
              {
                data: [this.state.normal, this.state.broken],
                backgroundColor: ["mediumseagreen", "tomato"]
              }
            ],

            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: [this.state.nl, this.state.bl]
          }}
        />
      </Container>
    );
  }
}
