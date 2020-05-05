Sub FillWorkingCy_new()

Dim wb As ThisWorkbook
Dim worksheets As Worksheet
Dim i, j As Variant
Dim s1_range, s2_range, u1_range, u2_range As Range
'Dim c1, c2, c3 As Range


Set s1_range = ThisWorkbook.worksheets("Simple Working Subs").Range("C2:C3535") 's_title number
Set u1_range = ThisWorkbook.worksheets("Use").Range("F2:F403") ' u_usage

Set s2_range = ThisWorkbook.worksheets("Simple Working Subs").Range("G2: G3535") ' s_usage
Set u2_range = ThisWorkbook.worksheets("Use").Range("B2: B403") 'u_title number


For i = 2 To 3535 's
    For j = 2 To 403  'u
        If u1_range.Cells.Rows(j).Interior.Color = RGB(198, 224, 180) Then ' the green colored cell
            If u2_range.Cells.Rows(j).Value = s1_range.Cells.Rows(i).Value Then 'title number the same
                If IsNull(s2_range.Cells.Rows(i).Value) Or IsEmpty(s2_range.Cells.Rows(i).Value) Or s2_range.Cells.Rows(i).Value = 0 Then
                'if s_usage is blank or 0 then fill the value
                    s2_range.Cells.Rows(i).Value = u1_range.Cells.Rows(j).Value
                End If
            End If
        End If
    Next j
Next i

End Sub
