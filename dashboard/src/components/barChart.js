import React, { PureComponent } from 'react';
import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';


export const BarGraph = (props) => {
    return (
      <ResponsiveContainer width="100%" height={400}>
        <BarChart
          width={500}
          height={300}
          data={props.data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey={props.xAxisKey} />
          <YAxis />
          <Tooltip />
          <Legend payload={[
          { value: props.item1Name, type: "line", id: props.item1, color: "#8884d8" },
          { value: props.item2Name, type: "line", id: props.item2, color: "#82ca9d" }
        ]}/>
          <Bar dataKey={props.item1} fill="#8884d8" />
          <Bar dataKey={props.item2} fill="#82ca9d" />
        </BarChart>
      </ResponsiveContainer>
    );
  }