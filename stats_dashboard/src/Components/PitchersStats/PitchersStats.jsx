import styles from '../PitchersStats/PitchersStats.module.css'
import Papa from 'papaparse';
import { useEffect, useState, useMemo } from 'react';
import React from 'react';

function PitchersStats() {
  const [data, setData] = useState([]);
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });

  useEffect(() => {
    fetch('assets/ranked_pitchers.csv')
      .then((res) => res.text())
      .then((text) => {
        Papa.parse(text, {
          header: true,
          dynamicTyping: true,
          complete: (results) => setData(results.data.filter(r => Object.keys(r).length > 1)), // filter empty rows
        });
      });
  }, []);

  // compute median (per column)
  const columnMedians = useMemo(() => {
    if (data.length === 0) return {};

    const medians = {};
    const columns = Object.keys(data[0]);

    columns.forEach((col) => {
      const nums = data
        .map((row) => row[col])
        .filter((v) => typeof v === "number" && !isNaN(v))
        .sort((a, b) => a - b);

      if (nums.length > 0) {
        const mid = Math.floor(nums.length / 2);
        medians[col] = nums.length % 2 !== 0
          ? nums[mid]
          : (nums[mid - 1] + nums[mid]) / 2;
      }
    });

    return medians;
  }, [data]);

  // sort data when sortConfig changes
  const sortedData = useMemo(() => {
    if (!sortConfig.key) return data;

    return [...data].sort((a, b) => {
      const aVal = a[sortConfig.key];
      const bVal = b[sortConfig.key];

      if (aVal === bVal) return 0;

      // numeric vs string sorting
      if (typeof aVal === 'number' && typeof bVal === 'number') {
        return sortConfig.direction === 'asc' ? aVal - bVal : bVal - aVal;
      } else {
        return sortConfig.direction === 'asc'
          ? String(aVal).localeCompare(String(bVal))
          : String(bVal).localeCompare(String(aVal));
      }
    });
  }, [data, sortConfig]);

  // handle header click
  const handleSort = (col) => {
    setSortConfig((prev) => {
      if (prev.key === col) {
        // toggle asc/desc
        return { key: col, direction: prev.direction === 'asc' ? 'desc' : 'asc' };
      } else {
        return { key: col, direction: 'asc' };
      }
    });
  };

  if (data.length === 0) return <p>Loading...</p>;

  return (
    <table className={styles.table}>
      <thead>
        <tr>
          {Object.keys(data[0]).map((col, i) => (
            <th key={i} onClick={() => handleSort(col)}>
              {col}
              {sortConfig.key === col && (sortConfig.direction === 'asc' ? ' 🔼' : ' 🔽')}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {sortedData.map((row, i) => (
          <tr key={i}>
            {Object.entries(row).map(([col, val], j) => {
              const median = columnMedians[col];
              let cellClass = "";

              if (typeof val === "number" && !isNaN(val) && median !== undefined) {
                if (val > median) cellClass = styles.good;
                else if (val < median) cellClass = styles.bad;
              }

              return (
                <td key={j} className={cellClass}>
                  {val}
                </td>
              );
            })}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default PitchersStats;
