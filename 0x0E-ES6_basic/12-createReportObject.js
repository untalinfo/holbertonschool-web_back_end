export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(allEmployees) {
      return Object.keys(allEmployees).length;
    },
  };
}
