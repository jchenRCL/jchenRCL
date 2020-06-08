Option Explicit

Sub toLowerCase()

Dim Workbook As ThisWorkbook
Dim Worksheet As Worksheets

Dim strText As Range
Dim strTextCase As Range
Dim cell As Range

Set strText = ThisWorkbook.Worksheets("Sheet1").Range("B2:B1394")

For Each cell In strText

' LCase is a function in vba to convert alphabets to lower case, UCase does the opposite

cell.Value = LCase(cell)

Next cell


End Sub

