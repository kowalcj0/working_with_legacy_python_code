from abc import ABC, abstractmethod
from typing import List


class QuarterlyReportGenerator:

    def generate(self) -> str:
        results = self.database.queryResults(beginDate, endDate)
        page_text: str = """<html><head><title>
        Quarterly Report
        "</title></head><body><table>"""
        if results.size() != 0:
            for it in results:
                page_text += "<tr>"
                page_text += "<td>" + it.department + "</td>"
                page_text += "<td>" + it.manager + "</td>"
                np = f"<td>${it.netProfit / 100}</td>"
                print(np)
                oe = f"<td>${it.operatingExpense / 100}</td>"
                print(oe)
                page_text += "</tr>"
        else:
            page_text += "No results for this period"
        page_text += "</table></body></html>"
        return page_text

    # ... more code


# TODO:
#  we need to make to the code is to add a header row for the HTML table it’s producing.
#  The header row should look something like this:
# "<tr><td>Department</td><td>Manager</td><td>Profit</td><td>Expenses</td></tr>"
# Furthermore, let’s suppose that this is a huge class and that it would take
# about a day to get the class in a test harness, and this is time that we just can’t
# afford right now.



class QuarterlyReportTableHeaderProducer():

    @staticmethod
    def make_header() -> str:
        return "<tr><td>Department</td><td>Manager</td><td>Profit</td><td>Expenses</td>"


class QuarterlyReportGenerator:

    # we can now instantiate header producer and add the header wherever we want
    def generate(self) -> str:
        results = self.database.queryResults(beginDate, endDate)
        page_text: str = """<html><head><title>
        Quarterly Report
        "</title></head><body><table>"""
        header_produce = QuarterlyReportTableHeaderProducer()
        page_text += header_produce
        if results.size() != 0:
            for it in results:
                page_text += "<tr>"
                #...


# The only reason we’re doing it is to get out of a bad dependency situation


class HTMLGenerator(ABC):

    @staticmethod
    @abstractmethod
    def generate() -> str:
        raise NotImplementedError


class QuarterlyReportTableHeaderGenerator(HTMLGenerator):

    @staticmethod
    def make_header() -> str:
        return "<tr><td>Department</td><td>Manager</td><td>Profit</td><td>Expenses</td>"

    # we can now instantiate header producer and add the header wherever we want
    def generate(self) -> str:
        results = self.database.queryResults(beginDate, endDate)
        page_text: str = """<html><head><title>
        Quarterly Report
        "</title></head><body><table>"""
        page_text += self.make_header()
        if results.size() != 0:
            for it in results:
                page_text += "<tr>"
                #...


class QuarterlyReportGenerator(HTMLGenerator):

    def generate(self) -> str:
        results = self.database.queryResults(beginDate, endDate)
        page_text: str = """<html><head><title>
    Quarterly Report
    "</title></head><body><table>"""
        if results.size() != 0:
            for it in results:
                page_text += "<tr>"
                # ...

