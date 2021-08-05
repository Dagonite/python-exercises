from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import List

FIXED_VACATION_DAYS_PAYOUT = 5  # fixed num of vacation days that can be paid out


class VacationDaysShortageError(Exception):
    """Custom error that is raised when not enough vacation days are available."""

    def __init__(self, requested_days: int, remaining_days: int, message: str) -> None:
        self.requested_days = requested_days
        self.remaining_days = remaining_days
        self.message = message
        super().__init__(message)


class Role(Enum):
    """Employee roles."""

    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""

    name: str
    role: Role
    vacation_days: int = 20

    @abstractmethod
    def pay(self) -> None:
        """Method to call when paying an employee."""

    def take_a_holiday(self) -> None:
        """Let the employee take a holiday."""

        if self.vacation_days < 1:
            raise VacationDaysShortageError(
                requested_days=1,
                remaining_days=self.vacation_days,
                message="You don't have any holidays left. Now back to work, you!",
            )
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")

    def payout_a_holiday(self) -> None:
        """Let the employee get paid for unused holidays."""

        # check that there are enough vacation days left for a payout
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise VacationDaysShortageError(
                requested_days=FIXED_VACATION_DAYS_PAYOUT,
                remaining_days=self.vacation_days,
                message="You don't have enough holidays left over for a payout",
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate: float = 15.45
    hours_worked: int = 9

    def pay(self) -> None:
        print(f"Paying employee {self.name} a hourly rate of £{self.hourly_rate} for {self.hours_worked} hours")


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 2500

    def pay(self) -> None:
        print(f"Paying employee {self.name} a monthly salary of £{self.monthly_salary}")


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, new_employee: Employee) -> None:
        """Add a new employee to the list of employees."""
        self.employees.append(new_employee)

    def add_employees(self, new_employees: List[Employee]) -> None:
        """Add a list of new employees to the list of employees."""
        for new_employee in new_employees:
            self.employees.append(new_employee)

    def find_employees_by_role(self, role: Role) -> List[Employee]:
        """Find all employees with a particular role in the employee list."""
        return [employee for employee in self.employees if employee.role is role]


if __name__ == "__main__":
    # create company named dagonite
    dagonite = Company()

    # add multiple employees at once
    dagonite.add_employees(
        [
            SalariedEmployee(name="Louis", role=Role.MANAGER),
            HourlyEmployee(name="Brenda", role=Role.PRESIDENT),
            HourlyEmployee(name="Tim", role=Role.INTERN),
        ]
    )

    # add single employee
    dagonite.add_employee(SalariedEmployee(name="Adam", role=Role.INTERN))

    # print employees in certain roles
    print(dagonite.find_employees_by_role(Role.VICEPRESIDENT))
    print(dagonite.find_employees_by_role(Role.MANAGER))
    print(dagonite.find_employees_by_role(Role.INTERN))
    print(dagonite.find_employees_by_role(Role.WORKER))

    # pay louis
    louis = dagonite.employees[0]
    louis.pay()

    # louis goes on holiday
    for _ in range(5):
        louis.take_a_holiday()

    # louis gets holiday payout
    louis.payout_a_holiday()
