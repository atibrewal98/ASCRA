import React, { PureComponent } from 'react';
import { ComposedChart, Line, Bar, Brush, ReferenceLine, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export const BarLineGraph = (props) => {
    return (
      <ResponsiveContainer width="100%" height={400}>
        <ComposedChart
          width={550}
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
          { value: props.item2Name, type: "bar", id: props.item2, color: "#82ca9d" }
        ]}/>
        <Brush dataKey={props.xAxisKey} height={30} stroke="#ffc658" />
            <ReferenceLine y={0} stroke="#000" />
            <Bar dataKey={props.item2} fill="#82ca9d" />
            <Line type="monotone" dataKey={props.item1} stroke="#8884d8" />
        </ComposedChart>
      </ResponsiveContainer>
    );
  }