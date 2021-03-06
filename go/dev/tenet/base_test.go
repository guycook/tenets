package tenet_test

import (
	"testing"

	gc "gopkg.in/check.v1"

	jc "github.com/juju/testing/checkers"
	"github.com/lingo-reviews/tenets/go/dev/api"
	"github.com/lingo-reviews/tenets/go/dev/tenet"
	tt "github.com/lingo-reviews/tenets/go/dev/tenet/testing"
)

func Test(t *testing.T) {
	gc.TestingT(t)
}

type baseSuite struct {
	tt.TenetSuite
}

var _ = gc.Suite(&baseSuite{})

func (s *baseSuite) SetUpTest(c *gc.C) {
	s.Tenet = &tenet.Base{}
	s.Tenet.SetInfo(tenet.Info{Name: "baseTestTenet"})
	s.TenetSuite.SetUpTest(c)
}

func (s *baseSuite) TestContextFull(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	// no regisitered issues should mean there is no context, which should
	// mean all contexts have been matched ...
	s.assertCxtFull(c, true)

	// ... and thus adding a new comment with a new context means we have a
	// context that hasn't matched.
	b.RegisterIssue("issue_with_first_comment_ctx", tenet.AddComment("first comment", tenet.FirstComment))
	s.assertCxtFull(c, false)

	// Add a smell which raises the above issue for every line.
	b.SmellLine(func(r tenet.Review, n int, line []byte) error {
		r.RaiseLineIssue("issue_with_first_comment_ctx", n, n)
		return nil
	})

	// Review some code, raise the issue.
	s.CheckSRC(c, "package mock", []tt.ExpectedIssue{
		{
			Text:    "package mock",
			Comment: "first comment",
		}}...)

	// Assert the context is now matched.
	s.assertCxtFull(c, true)
}

func (s *baseSuite) TestDefaultContextIsNeverFull(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	// no regisitered issues should mean there is no context, which should
	// mean all contexts have been matched ...
	s.assertCxtFull(c, true)

	// ... and thus adding a new comment with a new context means we have a
	// context that hasn't matched.
	b.RegisterIssue("issue_with_first_comment_ctx",
		tenet.AddComment("first comment", tenet.FirstComment),
		tenet.AddComment("default comment", tenet.DefaultComment),
	)
	s.assertCxtFull(c, false)

	// Add a smell which raises the above issue for every line.
	b.SmellLine(func(r tenet.Review, n int, line []byte) error {
		r.RaiseLineIssue("issue_with_first_comment_ctx", n, n)
		return nil
	})

	// Review some code, raise the issue.
	s.CheckSRC(c, "package mock\n// next line", []tt.ExpectedIssue{
		{
			Text:    "package mock",
			Comment: "first comment",
		}, {
			Text:    "// next line",
			Comment: "default comment",
		}}...)

	// assert the context is still not matched.
	s.assertCxtFull(c, false)
}

func (s *baseSuite) TestSkipContextSkipsIssue(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	// no regisitered issues should mean there is no context, which should
	// mean all contexts have been matched ...
	s.assertCxtFull(c, true)

	// ... and thus adding a new comment with a new context means we have a
	// context that hasn't matched.
	b.RegisterIssue("issue_with_first_comment_ctx",
		tenet.AddComment("first comment", tenet.FirstComment),
		tenet.AddComment("third comment", tenet.ThirdComment),
	)
	s.assertCxtFull(c, false)

	// Add a smell which raises the above issue for every line.
	b.SmellLine(func(r tenet.Review, n int, line []byte) error {
		r.RaiseLineIssue("issue_with_first_comment_ctx", n, n)
		return nil
	})

	// Review some code, raise the issue.
	s.CheckSRC(c, "package mock\n// 2nd line\n// 3rd line", []tt.ExpectedIssue{
		{
			Text:    "package mock",
			Comment: "first comment",
		}, {
			Text:    "// 3rd line",
			Comment: "third comment",
		}}...)

	s.assertCxtFull(c, true)
}

func (s *baseSuite) TestHardCodedDefaultFindsEveryIssue(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	// Adding an issue with no comment context defaults to hardcoded default
	// ...
	b.RegisterIssue("issue_with_every_line")

	// Add a smell which raises the above issue for every line.
	b.SmellLine(func(r tenet.Review, n int, line []byte) error {
		r.RaiseLineIssue("issue_with_every_line", n, n)
		return nil
	})

	// ... and picks up every issue.
	s.CheckSRC(c, "package mock\n// 2nd line\n// 3rd line", []tt.ExpectedIssue{
		{
			Text:    "package mock",
			Comment: "Issue Found",
		}, {
			Text:    "// 2nd line",
			Comment: "Issue Found",
		}, {
			Text:    "// 3rd line",
			Comment: "Issue Found",
		}}...)

	s.assertCxtFull(c, false)
}

func (s *baseSuite) TestDefaultFindsEveryIssue(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	// Adding an issue with no comment context defaults to hardcoded default
	// ...
	b.RegisterIssue("issue_with_every_line", tenet.AddComment("Custom Default Msg", tenet.DefaultComment))

	// Add a smell which raises the above issue for every line.
	b.SmellLine(func(r tenet.Review, n int, line []byte) error {
		r.RaiseLineIssue("issue_with_every_line", n, n)
		return nil
	})

	// ... and picks up every issue.
	s.CheckSRC(c, "package mock\n// 2nd line\n// 3rd line", []tt.ExpectedIssue{
		{
			Text:    "package mock",
			Comment: "Custom Default Msg",
		}, {
			Text:    "// 2nd line",
			Comment: "Custom Default Msg",
		}, {
			Text:    "// 3rd line",
			Comment: "Custom Default Msg",
		}}...)

	s.assertCxtFull(c, false)
}

func (s *baseSuite) TestSkipFallsBackToCustomDefaultFindsEveryIssue(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	// Adding an issue with no comment context defaults to hardcoded default
	// ...
	b.RegisterIssue("issue_with_every_line",
		tenet.AddComment("first comment", tenet.FirstComment),
		tenet.AddComment("third comment", tenet.ThirdComment),
		tenet.AddComment("Custom Default Msg"),
	)

	// Add a smell which raises the above issue for every line.
	b.SmellLine(func(r tenet.Review, n int, line []byte) error {
		r.RaiseLineIssue("issue_with_every_line", n, n)
		return nil
	})

	// ... and picks up every issue.
	s.CheckSRC(c, `
package mock
// 2nd line
// 3rd line
// 4th line
`[1:], []tt.ExpectedIssue{
		{
			Text:    "package mock",
			Comment: "first comment",
		}, {
			Text:    "// 2nd line",
			Comment: "Custom Default Msg",
		}, {
			Text:    "// 3rd line",
			Comment: "third comment",
		}, {
			Text:    "// 4th line",
			Comment: "Custom Default Msg",
		}, {
			Text:    "", // new line at end of file
			Comment: "Custom Default Msg",
		}}...)

	s.assertCxtFull(c, false)
}

func (s *baseSuite) assertCxtFull(c *gc.C, expected bool) {
	c.Assert(tenet.AreAllContextsMatched(s.Review.(tenet.BaseReview)), gc.Equals, expected)
}

func (s *baseSuite) TestRegisterOption(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	opts := []*api.Option{{
		Name:  "key",
		Value: "value",
	}}

	err := b.MixinConfigOptions(opts)
	c.Assert(err, gc.ErrorMatches, `tenet has no option \"key\"`)

	v := b.RegisterOption("key", "default", "usage string")
	c.Assert(*v, gc.Equals, "default")
	c.Assert(b.MixinConfigOptions(opts), jc.ErrorIsNil)
	c.Assert(*v, gc.Equals, "value")
}

// TODO(waigani) table based test of all context combinations.
func (s *baseSuite) TestContextFirstInEveryFile(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	b.RegisterIssue("issue_with_every_line",
		tenet.AddComment("first comment", tenet.FirstComment, tenet.InEveryFile),
	)

	// Add a smell which raises the above issue for every line.
	b.SmellLine(func(r tenet.Review, n int, line []byte) error {
		r.RaiseLineIssue("issue_with_every_line", n, n)
		return nil
	})

	// Add three files with a line of code.
	src := `
package mock
// 2nd line
// 3rd line
// 4th line
`[1:]
	files := []string{
		s.TmpFile(c, src),
		s.TmpFile(c, src),
		s.TmpFile(c, src),
	}

	expectedIssues := []tt.ExpectedIssue{
		{
			Text:     "package mock",
			Comment:  "first comment",
			Filename: files[0],
		}, {
			Text:     "package mock",
			Comment:  "first comment",
			Filename: files[1],
		}, {
			Text:     "package mock",
			Comment:  "first comment",
			Filename: files[2],
		},
	}

	s.CheckFiles(c, files, expectedIssues...)

	// Assert the context is now matched.
	s.assertCxtFull(c, false)
}

// TODO(waigani) table based test of all context combinations.
func (s *baseSuite) TestContextDefaultInSecondFile(c *gc.C) {
	b := s.Tenet.(*tenet.Base)

	b.RegisterIssue("issue_with_every_line",
		tenet.AddComment("first comment", tenet.DefaultComment, tenet.InSecondFile),
	)

	// Add a smell which raises the above issue for every line.
	b.SmellLine(func(r tenet.Review, n int, line []byte) error {
		r.RaiseLineIssue("issue_with_every_line", n, n)
		return nil
	})

	// Add three files with a line of code.
	src := `
package mock
// 2nd line
// 3rd line
// 4th line
`[1:]

	src2 := `
package secondMock
// 2.2nd line
// 2.3rd line
// 2.4th line
`[1:]

	files := []string{
		s.TmpFile(c, src),
		s.TmpFile(c, src2),
		s.TmpFile(c, src),
	}

	expectedIssues := []tt.ExpectedIssue{
		{
			Text:     "package secondMock",
			Comment:  "first comment",
			Filename: files[1],
		}, {
			Text:     "// 2.2nd line",
			Comment:  "first comment",
			Filename: files[1],
		}, {
			Text:     "// 2.3rd line",
			Comment:  "first comment",
			Filename: files[1],
		}, {
			Text:     "// 2.4th line",
			Comment:  "first comment",
			Filename: files[1],
		}, {
			Text:    "", // new line at end of file
			Comment: "first comment",
		},
	}

	s.CheckFiles(c, files, expectedIssues...)

	// TODO(waigani) this should be true. Once we sniff the last node/line of
	// a file, we can set DefaultComment|FileContext as matched
	s.assertCxtFull(c, false)
}
